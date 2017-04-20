def userRole_to_viewFile():
  from flask import session
  userRole = session['userRole'] if 'userRole' in session else 'player'
  viewFile = 'user/dashboard-%s.html' % userRole
  return viewFile