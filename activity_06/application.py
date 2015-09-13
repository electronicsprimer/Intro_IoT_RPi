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
from flask import Flask             # Import the Flask class from the flask module
import RPi.GPIO as GPIO             # Import GPIO library
import time                         # Import time library for sleep delay

led_pin = 7                         # Pin number for LED

def blink_led(num):
    GPIO.setmode(GPIO.BOARD)            # Use board pin numbering
    GPIO.setup(led_pin, GPIO.OUT)       # Setup GPIO Pin 7 to OUT
    try:
        for i in range(num):
            GPIO.output(led_pin,True)   # Turn on GPIO pin 7
            time.sleep(1)               # Hold the LED ON for 1 second
            GPIO.output(led_pin,False)  # Turn on GPIO pin 7
            time.sleep(1)               # Hold the LED ON for 1 second
    except KeyboardInterrupt:  
        # here you put any code you want to run before the program   
        # exits when you press CTRL+C  
        print "Quiting..."  
    finally:  
        GPIO.cleanup() # this ensures a clean exit   

app = Flask(__name__)               # Instantiate a Flask object

# Use the route() decorator to tell Flask what URL should trigger our function
@app.route('/')                 
# The function is given a name which is also used to generate URLs 
def hello_world():              
    blink_led(3)
    return 'Hello World!'
# use the run() function to run the local server with our application
if __name__ == '__main__':
#    app.run()                  # Only accessible from this machine
    app.run(host='0.0.0.0')     # Accessible from the outside world
 
