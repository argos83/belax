import time
from base_step import RedmineStep

class Login(RedmineStep):

    NAME = "Login"
    DESCRIPTION = "Logs in with the given user and password"
    TAGS = ["users"]
    
    def run(self, username, password):
        if username == "guest":
            raise Exception("404")
        time.sleep(1)
        return "[%s]" % (username)