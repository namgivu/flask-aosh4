from app import *


@app.route('/statistic/leading-board')
def statistic_leading_board():
  template=userRole_to_dashboardView()
  return render_template('statistic/leading-board.html', **locals() )


@app.route('/statistic/mission-board')
def statistic_mission_board():
  template=userRole_to_dashboardView()
  return render_template('statistic/mission-board.html', **locals() )


@app.route('/statistic/all-on-going')
def statistic_all_on_going():
  template=userRole_to_dashboardView()
  userRole = currentUserRole()
  return render_template('statistic/all-on-going.html', **locals() )
