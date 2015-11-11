import os
from test_cases.create_issue import CreateIssue
from test_cases.create_project import CreateProject

from marvin.report.observers.event_logger import EventLogger
from marvin.report.observers.elk_reporter import ELKReporter
from marvin.data.data_providers.json_data import JSONData
from marvin import Suite

class RedmineTestSuite(Suite):

    def __init__(self):
        profile = os.environ.get("PROFILE", "test")

        # Depending on the profile we get from the environment
        # we could add different observers with different settings
        event_logger = EventLogger()

        if profile == "prod":
            elk_reporter = ELKReporter("http://localhost:9200/", "logstash-belatrix-2015-10-31")
    
    def tests(self):
        return [
        CreateIssue(
            JSONData("/home/seba/git/personal/belax/redmine/test_cases/create_issue.json")
        )
        ]


if __name__ == '__main__':
    RedmineTestSuite().execute()