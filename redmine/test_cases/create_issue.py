import time
import sys

from marvin import TestScript

from steps.redmine.login import Login
from steps.redmine.create_project import CreateProject
from steps.redmine.create_issue import CreateIssue as CreateIssueStep


class CreateIssue(TestScript):

    NAME = "Create Issue Test"
    DESCRIPTION = "Check that issues can be created properly"
    TAGS = ["issues", "wip"]

    def setup(self, data):
        # Login in the redmine
        login = data['login']
        after = lambda step, result: sys.stdout.write("We could have here test context specific assertions\n")
        
        self.session = Login().doing_after(after).execute(login['user'],
                                                          login['password'])
        
        # Create a project
        project = data['project']
        self.project = CreateProject().execute(self.session, 
                                               project['summary'],
                                               project['description'])

    def run(self, data):
        # Create an issue with the given settings
        CreateIssueStep().execute(self.session,
                                  self.project,
                                  data['summary'],
                                  data.get('description', "Default description"))

    def tear_down(self, _data):
        # Clean up / logout, etc
        pass