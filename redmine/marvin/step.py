import time

class Step(object):

    def execute(self, *args, **kargs):
        start = time.time()
        result = self.run(*args, **kargs)
        print "Took", time.time() - start, "seconds"

    def run(self, *args, **kargs):
        raise NotImplementedError("Method run must be redefined")