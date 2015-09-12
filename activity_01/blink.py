"""
  09/01/2015
  Author: Makerbro
  Platforms: Raspberry Pi (Raspbian)
  Language: Python
  File: blink.py
  ------------------------------------------------------------------------
  Description: 
  Blinks an LED.
  ------------------------------------------------------------------------
  Please consider buying products from ACROBOTIC to help fund future
  Open-Source projects like this! We’ll always put our best effort in every
  project, and release all our design files and code for you to use. 
  https://acrobotic.com/
  ------------------------------------------------------------------------
  License:
  Beerware License; if you find the code useful, and we happen to cross 
  paths, you're encouraged to buy us a beer. The code is distributed hoping
  that you in fact find it useful, but  without warranty of any kind.
"""
import RPi.GPIO as GPIO         # Import GPIO library
import time                     # Import time library for sleep delay

led_pin = 7                     # Pin number for LED

GPIO.setmode(GPIO.BOARD)        # Use board pin numbering
GPIO.setup(led_pin, GPIO.OUT)   # Setup GPIO Pin 7 to OUT

while 1:
    try:
        GPIO.output(7,True)     # Turn on GPIO pin 7
        time.sleep(1)           # Hold the LED ON for 1 second
        GPIO.output(7,False)    # Turn on GPIO pin 7
        time.sleep(1)           # Hold the LED ON for 1 second
    except KeyboardInterrupt:  
        # here you put any code you want to run before the program   
        # exits when you press CTRL+C  
        print "Quiting..."  
    except:  
        # this catches ALL other exceptions including errors.  
        # You won't get any error messages for debugging  
        # so only use it once your code is working  
        print "Other error or exception occurred!"  
    finally:  
        GPIO.cleanup() # this ensures a clean exit   
