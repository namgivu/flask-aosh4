from app import *


@app.route('/user/switch-role')
def user_switch_role():
  return render_template('user/switch-role.html')


@app.route('/user/dashboard')
def user_dashboard():
  return render_template('user/dashboard.html')

