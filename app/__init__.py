#the Flask app
from flask import Flask
app = Flask(__name__)


#app config
app.config.from_object('config.BaseConfig')


#common modules
from flask import \
  render_template,\
  url_for

from werkzeug.utils import redirect


#in-app util
from util import *


#route handler/controller
from controller import *


#set session secret key
app.secret_key = 'HumGfpMS4Mx3QSXk'
app.config['SESSION_TYPE'] = 'filesystem'