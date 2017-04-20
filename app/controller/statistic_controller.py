from app import *


@app.route('/statistic/leading-board')
def statistic_leading_board():
  return render_template(
    'statistic/leading-board.html',
    viewFile=userRole_to_viewFile(),
  )
