from app import *


@app.route('/user/switch-role')
def user_switch_role():
  return render_template('user/switch-role.html')


@app.route('/user/dashboard-player')
def user_dashboard_player():
  return render_template('user/dashboard-player.html')

