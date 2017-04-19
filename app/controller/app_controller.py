from app import app


@app.route('/')
def app_index():
  return 'flask-aosh4'
