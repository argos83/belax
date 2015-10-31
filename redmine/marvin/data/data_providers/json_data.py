from marvin.data.data import Data
import json

class JSONData(Data):

    def __init__(self, *args, **kargs):
        super(JSONData, self).__init__(*args, **kargs)
        with open(self._source_id, "r") as fd:
            self.json = json.load(fd)

    def setup_data(self):
        return self.json.get('setup', {})

    # GENERATOR
    def iteration_data(self):
        for it_data in self.json.get('iterations', []):
            yield it_data

    def tear_down_data(self):
        return self.json.get('tear_down', {})