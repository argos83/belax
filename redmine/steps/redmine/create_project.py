import time
from base_step import RedmineStep

class CreateProject(RedmineStep):
    
    NAME = "Create Project"
    DESCRIPTION = "Creates a new project in redmine with the given settings"
    TAGS = ["projects"]

    def run(self, session, name, description):
        time.sleep(1)
        return name