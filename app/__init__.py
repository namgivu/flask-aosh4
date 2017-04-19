#the Flask app
from flask import Flask
app = Flask(__name__)

#app config
app.config.from_object('config.BaseConfig')

#route handler/controller
from controller import *