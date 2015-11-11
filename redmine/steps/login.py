import time
from marvin import Step

class Login(Step):

    NAME = "Login"
    DESCRIPTION = "Logs in with the given user and password"
    TAGS = ["redmine", "users"]
    
    def run(self, username, password):
        if username == "guest":
            raise KeyError("404")
        time.sleep(1)
        return "[%s]" % (username)