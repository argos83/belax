import time
from marvin.step import Step

class Login(Step):
    
    def run(self, username, password):
        print "login in with", username, "and", password
        if username == "guest":
            raise Exception("404")
        time.sleep(1)
        return "[%s]" % (username)