import unittest
import time
from steps.login import Login
from steps.create_project import CreateProject
from marvin.report.event_logger import EventLogger

event_logger = EventLogger()

class RedmineTest(unittest.TestCase):


    def test_create_project(self):
        session = Login().execute("admin", "123")
        print "list projects"
        time.sleep(1)
        
        CreateProject().execute(session, "demo", "demo project")

        print "list projects again"
        time.sleep(1)
        print "list incremented by one"

    def test_create_ticket(self):
        session = Login().execute("guest", "123")

        CreateProject().execute(session, "demo", "demo project")
        print "create issue"
        time.sleep(1)
        print "list issues"
        time.sleep(1)
        print "project has 1 issue"


    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()