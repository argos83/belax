import time
from base_step import RedmineStep

class CreateIssue(RedmineStep):
    
    NAME = "Create Issue"
    DESCRIPTION = "Creates a new issue in the given project"
    TAGS = ["issues"]

    def run(self, session, project, name, description):
        print "Issue: %s.%s (%s)" % (project, name, description)
        time.sleep(1)