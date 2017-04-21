#region register app home path ref. http://flask.pocoo.org/docs/0.11/deploying/mod_wsgi/#creating-a-wsgi-file
#TODO add path right inside WSGI config file (learn on Django guide page)
import os, sys
APP_HOME = os.path.abspath( os.path.dirname(__file__) )
sys.path.insert(0, APP_HOME)
#endregion register app home path

#the app creation
from app import app as application

#set session secret key
application.secret_key = 'HumGfpMS4Mx3QSXk'
application.config['SESSION_TYPE'] = 'filesystem'