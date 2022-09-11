from aa_session import *

class CWEBS:
    AA_SESSION = None
    S_CURRENT_SESSION_NAME = None


CWEB_SESSION = CWEBS()

def get_web_session() -> CWEBS:
    global CWEB_SESSION
    return CWEB_SESSION

def set_web_session(cwebs:CWEBS):
    global CWEB_SESSION
    CWEB_SESSION = cwebs
