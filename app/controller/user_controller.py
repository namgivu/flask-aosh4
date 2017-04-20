from app import *


@app.route('/user/switch-role')
def user_switch_role():
  return render_template('user/switch-role.html')


@app.route('/user/dashboard-player')
def user_dashboard_player():
  return render_template('user/dashboard-player.html')

@app.route('/user/my-task')
def user_my_task():
  return render_template('user/base_task_board.html')

@app.route('/user/dashboard-giver')
def user_dashboard_giver():
  return render_template('user/dashboard-giver.html')
