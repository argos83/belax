import time
from marvin.report.publisher import Publisher, Events


class Step(object):

    def __init__(self):
        self._runtime_tags = []

    @property
    def name(self):
        return getattr(self.__class__, "NAME", self.__class__.__name__)

    @property
    def description(self):
        return getattr(self.__class__, "DESCRIPTION", "")

    @property
    def tags(self):
        return self._runtime_tags + self.__class__._class_tags()
       

    def tag(self, *tags):
        self._runtime_tags.extend(tags)

    def execute(self, *args, **kargs):
        start = int(time.time() * 1000)

        data = {"step": self,
                "args": args,
                "kargs": kargs,
                "timestamp": start}

        Publisher.notify(Events.STEP_STARTED, data)

        status = "PASSED"
        exception = None
        result = None

        try:
            result = self.run(*args, **kargs)
        except Exception, e:
            status = "FAILED"
            exception = e

        data = {"step": self,
                "result": result,
                "status": status,
                "start_time": start,
                "exception": exception,
                "timestamp": int(time.time() * 1000)}
        Publisher.notify(Events.STEP_ENDED, data)
        if exception:
            raise

        return result

    def run(self, *args, **kargs):
        raise NotImplementedError("Method run must be redefined")   

    @classmethod
    def _class_tags(cls):
        return cls._base_tags() + getattr(cls, 'TAGS', [])

    @classmethod
    def _base_tags(cls):
        tags = []
        for klass in cls.__bases__:
            if issubclass(klass, Step) and klass != Step:
                tags += klass._class_tags()
        return tags        