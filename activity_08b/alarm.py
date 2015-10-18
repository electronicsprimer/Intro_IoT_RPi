"""
  09/01/2015
  Author: Makerbro
  Platforms: Raspberry Pi (Raspbian)
  Language: Python
  File: alarm.py
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
import RPi.GPIO as GPIO             # Import GPIO library
import time                         # Import time library for sleep delay
import subprocess                   # Import subprocess module
import os

class Alarm(object):
    def __init__(self, mode=GPIO.BOARD):
        '''
            Initialize the pins, set them up
        '''
        self.pir_pin = 15
        self.led_pin = 7
        self.buzz_pin = 11
        self.output_dir = "static/"
        self.dev = "/dev/video0"
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)
        self.status = False

        GPIO.setmode(mode)
        GPIO.setup(self.buzz_pin, GPIO.OUT)      # Setup GPIO Pin 7 to OUT
        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.setup(self.pir_pin, GPIO.IN)

        self.pwm_obj = GPIO.PWM(self.buzz_pin,350)  # Frequency of sound 350Hz

        #time.sleep(30)
        self.pir_state_last = GPIO.input(self.pir_pin)

    def __exit__(self, type, value, traceback):
        GPIO.cleanup(self.pir_pin)
        GPIO.cleanup(self.led_pin)
        GPIO.cleanup(self.buzz_pin)

    def detect_motion(self):
        pir_state = GPIO.input(self.pir_pin)

        if pir_state == GPIO.HIGH and self.pir_state_last == GPIO.LOW:
          print("Motion started")
          return True

        self.pir_state_last = pir_state

        time.sleep(0.1)
        return False

    def blink_led(self):
        GPIO.output(self.led_pin,True)   # Turn on GPIO pin 7
        time.sleep(1)               # Hold the LED ON for 1 second
        GPIO.output(self.led_pin,False)  # Turn on GPIO pin 7
        time.sleep(1)               # Hold the LED ON for 1 second

    def play_sound(self):
        self.pwm_obj.start(50)     # start the PWM with the duty cycle at 50%
        time.sleep(1)
        self.pwm_obj.start(0)

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def capture_img(self):
        path = os.path.join(self.output_dir,"snapshot.jpg")
        p = subprocess.Popen(["fswebcam","-r","640x480","-d",self.dev,"-q",path],
                             stderr=subprocess.STDOUT,
                             stdout=subprocess.PIPE)
        p.wait()
        out, err = p.communicate()
        p = subprocess.Popen(["chown","-R","pi:pi",self.output_dir],
                             stderr=subprocess.STDOUT,
                             stdout=subprocess.PIPE)
        p.wait()
        out, err = p.communicate()

    def run(self):
        while True:
            distance = self.range_cm()
            if distance is not None:
                if distance < 30:
                    self.status = True
                    self.capture_img()
            time.sleep(1)
   

if __name__ == "__main__":
    try:
        alarm = Alarm()
        while True:
            distance = alarm.range_cm()
            if distance:
                print("Distance %s cm" % distance)
            time.sleep(1)
    except KeyboardInterrupt:  
        # here you put any code you want to run before the program   
        # exits when you press CTRL+C  
        print "Quiting..."  
    finally:  
        GPIO.cleanup() # this ensures a clean exit   
