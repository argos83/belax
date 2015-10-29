import time
from marvin.step import Step

class CreateProject(Step):
    
    def run(self, session, name, description):
        print "Session", session, ": create project", name, "(", description, ")"
        time.sleep(1)