from app import app


@app.route('/')
def app_index():
  from flask import render_template
  return render_template('layout/base.html')


@app.before_request
def before_request_handler():
  from flask import g
  g.pageTitle = app.config['APP_NAME']
