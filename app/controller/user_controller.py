from app import *
import random
from flask import session


@app.route('/user/switch-role')
def user_switch_role():
  return render_template('user/switch-role.html')


@app.route('/user/dashboard-player')
def user_dashboard_player():
  session['userRole'] = app.config['USER_ROLE']['player']
  return render_template('user/dashboard-player.html')


@app.route('/user/player/my-board')
def user_player_my_board():
  days = range(1, 30)
  months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  names = ['Anonymous']
  chars = "abcdefghjiklmnopqrstw"
  for i in range(5):
    names.append(''.join(random.sample(chars,len(chars))))
  points = range(100, 1000)
  fake_data = []
  for i in range(5):
    data = {
      'day': random.choice(days),
      'month': random.choice(months),
      'point': random.choice(points),
      'name': random.choice(names)[:9]
    }
    if random.randint(1, 2) == 2:
      data['is_my_task'] = 1
    else:
      data['is_received_task'] = 1
    fake_data.append(data)
  return render_template('user/base_task_board.html', **locals())


@app.route('/user/player/mission-board')
def user_player_mission_board():
  days = range(1, 30)
  months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  names = ['Anonymous']
  chars = "abcdefghjiklmnopqrstw"
  for i in range(5):
    names.append(''.join(random.sample(chars,len(chars))))
  points = range(100, 1000)
  fake_data = []
  for i in range(5):
    data = {
      'day': random.choice(days),
      'month': random.choice(months),
      'point': random.choice(points),
      'name': random.choice(names)[:9],
      'is_other_task': 1
    }
    fake_data.append(data)
  return render_template('user/base_task_board.html', **locals())


@app.route('/user/dashboard-giver')
def user_dashboard_giver():
  session['userRole'] = app.config['USER_ROLE']['giver']
  return render_template('user/dashboard-giver.html')
