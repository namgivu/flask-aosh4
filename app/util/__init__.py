from flask import session


def currentUserRole():
  userRole = session['userRole'] if 'userRole' in session else 'player'
  return userRole



def userRole_to_dashboardView():
  userRole = currentUserRole()
  viewFile = 'user/dashboard-%s.html' % userRole
  return viewFile
