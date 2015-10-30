from publisher import Publisher
from events import Events

class EventLogger(object):

    def __init__(self):
        Publisher.subscribe(Events.STEP_STARTED, self.on_step_started)
        Publisher.subscribe(Events.STEP_ENDED, self.on_step_ended)

    def on_step_started(self, _event, data):
        step = data['step']

        print "%s: %s (%s)" % (step.name, step.description, ", ".join(step.tags))

    def on_step_ended(self, _event, data):
        step = data['step']
        duration = data['timestamp'] - data['start_time']
        print "[%s] %s (%d ms)" % (data['status'], step.name, duration)
