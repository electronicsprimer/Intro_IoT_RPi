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
import RPi.GPIO as GPIO                 # Import GPIO library
import time                             # Import time library for sleep delay

led_pin = 7                             # Pin number for LED
led_status = "OFF"
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin,False)

# -----------------------------------------------------------------------------
# API
# -----------------------------------------------------------------------------
# Use the route() decorator to tell Flask what URL should trigger our function
from flask import Flask, render_template, request, g
import json, datetime

app = Flask(__name__)                       # Instantiate a Flask object
@app.route('/')                 
def index():              
    templateData = {
        'title' : 'Welcome to the web-led control center'
    }
    return render_template('main.html', **templateData)

@app.route('/on', methods=['GET'])
def rpi_on():
    global led_status 
    led_status = "ON"
    GPIO.output(led_pin,True)
    return ('', 204)
 
@app.route('/off', methods=['GET'])
def rpi_off():
    global led_status 
    led_status = "OFF"
    GPIO.output(led_pin,False)
    return ('', 204)

# GET request to retrieve LED status
@app.route('/status', methods=['GET'])
def get_status():
    return json.dumps(led_status)

# POST request to set the LED status
@app.route('/status', methods=['POST'])
def post_status():
    req = request.get_json()
    if(req['status']):
      rpi_on()
    elif(not req['status']):
      rpi_off()
    return ('', 204)

# use the run() function to run the local server with our application
if __name__ == '__main__':
    try: 
        app.run(host='0.0.0.0',debug=True)      # Accessible from the outside world
    except KeyboardInterrupt:  
        print "Quiting..."  
    finally:  
        GPIO.cleanup() # this ensures a clean exit   
