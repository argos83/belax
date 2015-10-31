from test_cases.create_issue import CreateIssue
from test_cases.create_project import CreateProject

from marvin.report.event_logger import EventLogger
from marvin.data.data_providers.json_data import JSONData

if __name__ == '__main__':
    event_logger = EventLogger()
    CreateIssue().execute(JSONData("/home/seba/git/personal/belax/redmine/test_cases/create_issue.json"))