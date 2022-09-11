##############################################################################
# imports
##############################################################################
# sys path
import sys
sys.path.insert(0, "../aa")
sys.path.insert(0, "../file")

import glob

# aa staff
import aa_session_def_global_1940
from web_session import *
from file_session import *


# flask staff 
from flask import Flask, render_template, redirect, url_for, request, session
from flask_session import Session
from werkzeug.exceptions import abort


##############################################################################
# globals
##############################################################################

# Loaded session

S_STD_SESSION_NAME = "New standard session (Global 1940)"


# FLASK app 
app = Flask(__name__)
app.config.from_object(__name__) 
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_COOKIE_NAME"] = "axis_allies"
#app.config["SECRET_KEY"] ='osd(99092=36&462134kjKDhuIS_d23',
Session(app)

##############################################################################
# route / flask functions
##############################################################################

@app.route('/')
def me_status():
    aa_session = get_web_session()
    #print (session['S_CURRENT_SESSION_NAME']) 
    if aa_session.AA_SESSION == None:
        return render_template('index.html', header=get_aa_session_status(), info=" !!! No session loaded !!!")

    return render_template('session_status.html', header=get_aa_session_status(), aa_session=aa_session.AA_SESSION)

@app.route('/me_load')
def me_load():
    l_sessions = read_aa_sessions()
    return render_template('me_load.html', header="Load", sessions=l_sessions )

@app.route('/me_save')
def me_save():
    return render_template('me_save.html', header="Save", info="me_2" )

@app.route('/me_3')
def me_3():
    return render_template('me_3.html', header="me_3", info="me_3" )

@app.route('/me_4')
def me_4():
    return render_template('me_4.html', header="me_4", info="me_4" )

@app.route('/<string:session_str>')
def aa_session(session_str):
    aa_session = get_web_session()
    aa_session.AA_SESSION = get_aa_session(session_str)
    aa_session.S_CURRENT_SESSION_NAME = session_str

    return redirect(url_for('me_status'))

##############################################################################
# local/helper functions
##############################################################################
def read_aa_sessions() -> list:
    l_sessions = glob.glob("./sessions/*.aa")
    l_sessions.append(S_STD_SESSION_NAME)
    return l_sessions

def get_aa_session(session):
    aa_session = None
    if (session != S_STD_SESSION_NAME):
        aa_session = CFILE.load_session(session)
    else:
        aa_session = CAAI_Session(s_name            = "Global game 1940",
                                  aa_map            = C_MAP_GLOBAL_1940,
                                  i_round           = 1,
                                  l_aa_nations      = L_NATION_SETUP_GLOBAL_1940,
                                  aa_current_nation = CAAN_GERMANY,
                                  aa_current_phase  = CType.S_PH1_PURCHASE_REPAIR)
    return aa_session

def get_aa_session_status():
    s_status = "Status"
    aa_session = get_web_session()
    
    if (aa_session.S_CURRENT_SESSION_NAME == None):
        s_status = s_status + ": No session"
    else:
        s_status = s_status + f": {aa_session.S_CURRENT_SESSION_NAME}"

    return s_status