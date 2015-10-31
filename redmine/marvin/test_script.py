import time
from marvin.report.publisher import Publisher, Events


class TestScript(object):

    def setup(self, _data):
        pass

    def run(self, _data):
        raise NotImplementedError("Method run must be redefined")

    def tear_down(self, _data):
        pass


    @property
    def name(self):
        return getattr(self.__class__, "NAME", self.__class__.__name__)

    @property
    def description(self):
        return getattr(self.__class__, "DESCRIPTION", "")

    @property
    def tags(self):
        return getattr(self.__class__, "TAGS", [])

    def execute(self, data_provider):
        start = int(time.time() * 1000)
        data = {
        "test_script": self,
        "timestamp": start,
        "data": None}

        status = "PASSED"

        Publisher.notify(Events.TEST_STARTED, data)

        self.setup(data_provider.setup_data())

        for it_data in data_provider.iteration_data():
            self.run(it_data)


        self. tear_down(data_provider.tear_down_data())

        data = {"test_script": self,
                "status": status,
                "start_time": start,
                "timestamp": int(time.time() * 1000)}

        Publisher.notify(Events.TEST_ENDED, data)

    


