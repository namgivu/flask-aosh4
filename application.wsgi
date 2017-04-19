#region register app home path ref. http://flask.pocoo.org/docs/0.11/deploying/mod_wsgi/#creating-a-wsgi-file
#TODO add path right inside WSGI config file (learn on Django guide page)
import os, sys
APP_HOME = os.path.abspath( os.path.dirname(__file__) )
sys.path.insert(0, APP_HOME)
#endregion register app home path

from app import app as application
