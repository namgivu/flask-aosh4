from app import *
import random
from flask import session


@app.route('/user/switch-role')
def user_switch_role():
  return render_template('user/switch-role.html')


@app.route('/user/wallet')
def user_wallet():
  template = userRole_to_dashboardView()
  fake_data = []
  for i in range(5):
    data = {
      'id': i + 1
    }
    fake_data.append(data)
  return render_template('user/wallet.html', **locals())


@app.route('/user/dashboard-player')
def user_dashboard_player():
  session['userRole'] = app.config['USER_ROLE']['player']
  return render_template('user/dashboard-player.html')


@app.route('/user/player/my-board')
def user_player_my_board():
  session['userRole'] = app.config['USER_ROLE']['player']
  template = userRole_to_dashboardView()
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
      'id': i + 1,
      'day': random.choice(days),
      'month': random.choice(months),
      'point': random.choice(points),
      'name': random.choice(names)[:9],
      'completed': True if random.randint(1, 2) == 2 else False,
    }
    if random.randint(1, 2) == 2:
      data['is_my_task'] = 1
    else:
      data['is_received_task'] = 1
    fake_data.append(data)
  return render_template('user/base_task_board.html', **locals())


@app.route('/user/player/mission-board')
def user_player_mission_board():
  session['userRole'] = app.config['USER_ROLE']['player']
  template = userRole_to_dashboardView()
  days = range(1, 30)
  months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  names = ['Anonymous']
  skills = ['AI', 'Design', 'Video Content', 'Develop', 'Other']
  chars = "abcdefghjiklmnopqrstw"
  for i in range(5):
    names.append(''.join(random.sample(chars,len(chars))))
  points = range(100, 1000)
  fake_data = []
  for i in range(5):
    data = {
      'id': i + 1,
      'day': random.choice(days),
      'month': random.choice(months),
      'point': random.choice(points),
      'name': random.choice(names)[:9],
      'skill': random.choice(skills),
      'is_other_task': 1
    }
    fake_data.append(data)
  return render_template('user/base_task_board.html', **locals())


@app.route('/user/leader-board')
def user_leader_board():
  template = userRole_to_dashboardView()
  chars = "abcdefghjiklmnopqrstw"
  names = []
  for i in range(5):
    names.append(''.join(random.sample(chars,len(chars))))
  points = range(1, 1000)
  fake_data = []
  for i in range(20):
    data = {
      'rank': i + 1,
      'name': random.choice(names)[:9],
      'point': random.choice(points)
    }
    fake_data.append(data)
  return render_template('/user/leader_board.html', **locals())


@app.route('/user/dashboard-giver')
def user_dashboard_giver():
  session['userRole'] = app.config['USER_ROLE']['giver']
  return render_template('user/dashboard-giver.html')


@app.route("/user/giver/my-board")
def user_giver_my_board():
  session['userRole'] = app.config['USER_ROLE']['giver']
  template = userRole_to_dashboardView()
  role = 'giver'
  not_show_avatar = True
  days = range(1, 30)
  months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  names = ['Anonymous']
  skills = ['AI', 'Design', 'Video Content', 'Develop', 'Other']
  chars = "abcdefghjiklmnopqrstw"
  for i in range(5):
    names.append(''.join(random.sample(chars,len(chars))))
  points = range(100, 1000)
  fake_data = []
  for i in range(5):
    data = {
      'id': i + 1,
      'day': random.choice(days),
      'month': random.choice(months),
      'point': random.choice(points),
      'name': random.choice(names)[:9],
      'skill': random.choice(skills),
      'is_setting': 1,
      'completed': True if random.randint(1, 2) == 2 else False,
    }
    fake_data.append(data)
  return render_template('user/base_task_board.html', **locals())