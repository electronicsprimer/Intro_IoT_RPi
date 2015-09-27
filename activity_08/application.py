"""
  09/01/2015
  Author: Makerbro
  Platforms: Raspberry Pi (Raspbian)
  Language: Python
  File: application.py
  ------------------------------------------------------------------------
  Description: 
  ------------------------------------------------------------------------
  Please consider buying products from ACROBOTIC to help fund future
  Open-Source projects like this! We'll always put our best effort in every
  project, and release all our design files and code for you to use. 
  https://acrobotic.com/
  ------------------------------------------------------------------------
  License:
  Beerware License; if you find the code useful, and we happen to cross 
  paths, you're encouraged to buy us a beer. The code is distributed hoping
  that you in fact find it useful, but  without warranty of any kind.
"""
# -----------------------------------------------------------------------------
# GPIO
# -----------------------------------------------------------------------------
from alarm import Alarm

# -----------------------------------------------------------------------------
# API
# -----------------------------------------------------------------------------
# Use the route() decorator to tell Flask what URL should trigger our function
from flask import Flask, render_template, request, g
import json, datetime

app = Flask(__name__)                       # Instantiate a Flask object
alarm = Alarm(trig_pin=15,echo_pin=13)
active = False

@app.route('/')                 
def index():              
    templateData = {
        'title' : 'Welcome to the web-led control center'
    }
    return render_template('main.html', **templateData)

# GET request to retrieve LED status
@app.route('/status', methods=['GET'])
def get_status():
    global active
    global alarm
    if not active:
        return json.dumps({'status':-1})
    status = False
    distance = alarm.range_cm()
    if distance is not None:
        if distance < 10:
            alarm.capture_img()
            alarm.blink_led()
            alarm.play_sound()
            status = True
    return json.dumps({'status':status})

# POST request to set the LED status
@app.route('/activate', methods=['POST'])
def post_status():
    global active
    req = request.get_json()
    print req
    if(req['status']):
      active = True
    elif(not req['status']):
      active = False
    return ('', 204)

# use the run() function to run the local server with our application
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)      # Accessible from the outside world
