"""
  09/01/2015
  Author: Makerbro
  Platforms: Raspberry Pi (Raspbian)
  Language: Python
  File: sound.py
  ------------------------------------------------------------------------
  Description: 
  Uses PWM to generate sound from a piezoelectric transducer.
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
import RPi.GPIO as GPIO             # Import GPIO library
import time                         # Import time library for sleep delay

buzz_pin = 11                       # Pin number for buzzer

GPIO.setmode(GPIO.BOARD)            # Use board pin numbering
GPIO.setup(buzz_pin, GPIO.OUT)      # Setup GPIO Pin 7 to OUT
delay_ms = 0.1                      # delay time in milliseconds for holding each duty
                                    # cycle value
try:
    while True:
        # Loop through the frequency range ~100Hz to ~1.2KHz in increaments of 50
        for i in range(100,1200,50):
            pwm_obj = GPIO.PWM(buzz_pin,i)  # set pwm of buzz_pin to frequency "i"
            pwm_obj.start(0)                # start the PWM with the duty cycle at 50%
            # We want to make the sound increase in volume by adjusting the PWM duty cycle
            # from 5% to 95%
            for i in range(5,96,5):
                pwm_obj.ChangeDutyCycle(i) 
                time.sleep(delay_ms)
            # We want to make the sound increase in volume by adjusting the PWM duty cycle
            # from 95% to 5%
            for i in range(95,4,-5):
                pwm_obj.ChangeDutyCycle(i)
                time.sleep(delay_ms)
except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print "Quiting..."  
finally:  
    GPIO.cleanup() # this ensures a clean exit   
