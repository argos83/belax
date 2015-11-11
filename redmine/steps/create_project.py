import time
from marvin import Step

class CreateProject(Step):
    
    NAME = "Create Project"
    DESCRIPTION = "Creates a new project in redmine with the given settings"
    TAGS = ["redmine", "projects"]

    def run(self, session, name, description):
        time.sleep(1)