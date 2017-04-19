from app import app


@app.route('/auth/sign-in')
def auth_sign_in():
  from flask import render_template
  return render_template('auth/sign-in.html')


@app.route('/auth/sign-out')
def auth_sign_out():
  from flask import render_template
  return render_template('auth/sign-out.html')
