
class Data(object):

    def __init__(self, source_id):
        self._source_id = source_id

    def setup_data():
        raise NotImplementedError("Method must be redefined")

    # GENERATOR
    def iteration_data():
        raise NotImplementedError("Method must be redefined")

    def tear_down_data():
        raise NotImplementedError("Method must be redefined")
