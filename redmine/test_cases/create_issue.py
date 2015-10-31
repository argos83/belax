from marvin import TestScript

import time

from steps.redmine.login import Login
from steps.redmine.create_project import CreateProject
from steps.redmine.create_issue import CreateIssue as CreateIssueStep


class CreateIssue(TestScript):

    NAME = "Create Issue Test"
    DESCRIPTION = "Check that issues can be created properly"
    TAGS = ["issues", "wip"]

    def setup(self, data):
        login = data['login']
        self.session = Login().execute(login['user'], login['password'])

        project = data['project']
        self.project = CreateProject().execute(self.session, project['summary'], project['description'])

    def run(self, data):
        
        CreateIssueStep().execute(self.session, self.project, data['summary'], data.get('description', "Default description"))

    def tear_down(self, _data):
        print "log out"