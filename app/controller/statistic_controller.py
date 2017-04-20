from app import *


@app.route('/statistic/leading-board')
def statistic_leading_board():
  viewFile=userRole_to_viewFile()
  return render_template('statistic/leading-board.html', **locals() )


@app.route('/statistic/mission-board')
def statistic_mission_board():
  viewFile=userRole_to_viewFile()
  return render_template('statistic/mission-board.html', **locals() )
