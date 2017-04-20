from app import app
from flask import request, redirect, url_for, render_template, session


@app.route('/auth/sign-in', methods=["GET", "POST"])
def auth_sign_in():
  if 'login' in session or 'email' in request.form:
    session['login'] = 1
    return redirect(url_for('user_switch_role'))
  return render_template('auth/sign-in.html')


@app.route('/auth/sign-out')
def auth_sign_out():
  if 'login' in session:
    del session['login']
  return redirect(url_for('app_index'))
