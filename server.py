from bottle import route, run, view, static_file
from datetime import datetime as dt
from horoscope import generate_prophecies, check_month, pigga_said, pigga_said2
import os

@route("/static/<filename>")
def send_static(filename):
    return static_file(filename, root="static")

@route("/")
@view("shablon")
def index():
  now = dt.now()
  return {
    "date": f"{now.day} {check_month()} {now.year}"
  }

@route("/api/forecasts")
def api_forecasts():
  pr = generate_prophecies(1, 1)
  return {"prophecies": pr }

@route("/api/pigga")
def api_pigga():
  ps = pigga_said()
  return {"pigga_said": ps }

@route("/api/pigga2")
def api_pigga2():
  ps = pigga_said2()
  return {"pigga_said2": ps }

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)