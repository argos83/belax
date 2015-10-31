from marvin import TestScript

import time

from steps.redmine.login import Login
from steps.redmine.create_project import CreateProject as CreateProjectStep


class CreateProject(TestScript):

    def run(self):
        session = Login().execute("admin", "123")

        CreateProjectStep().execute(session, "demo", "demo project")
        #print "create issue"
        #print "list issues"
        #print "project has 1 issue"