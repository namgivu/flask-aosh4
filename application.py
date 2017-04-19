from app import app as application

application.debug=True
if __name__ == '__main__':
  application.run(host='0.0.0.0', debug=True, port=5000, threaded=True)