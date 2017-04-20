from app import *


@app.route('/user/switch-role')
def user_switch_role():
  return render_template('user/switch-role.html')

