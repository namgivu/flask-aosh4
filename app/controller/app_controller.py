from app import *


@app.before_request
def before_request_handler():
  from flask import g
  g.pageTitle = app.config['APP_NAME']


@app.route('/')
def app_index():
  return redirect(url_for('app_intro'))


def app_index_default():
  from flask import render_template
  return render_template('index.html')


@app.route('/intro')
def app_intro():
  return render_template('intro.html')


@app.before_first_request
def init_emptyTaskList_session():
  session['emptyTask'] = True
  session['emptyTask'] = False #TODO temporary set it False; turn it back on when this todo is coded "TODO place a button to remove emptyTask in session" ref. app/templates/user/dashboard.html:10
