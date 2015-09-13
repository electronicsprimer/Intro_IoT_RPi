"""
  09/01/2015
  Author: Makerbro
  Platforms: Raspberry Pi (Raspbian)
  Language: Python
  File: usb_camera.py
  ------------------------------------------------------------------------
  Requirements:
  This code requires the use of a USB camera:
  https://acrobotic.com/cam-00002

  Using the camera on Raspbian requires a capture program. Given that none
  is included with the default distribution, we need to install fswebcam
  or similar.  To do so we need to run on a terminal window the command:

  sudo apt-get install fswebcam
  ------------------------------------------------------------------------
  Description: 
  Uses the Popen module (subprocess) to run external commands to capture
  images from a connected USB camera.
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

output_dir = "/home/pi/pictures/"
dev = "/dev/video0"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
try:
    path = os.path.join(output_dir,"%m-%d-%y-%H%M.jpg")
    # run the command
    # fswebcam -r 640x480 -d /dev/video0 -q /path/to/picture/files
    #
    p = subprocess.Popen(["fswebcam","-r","640x480","-d",dev,"-q",path],
                         stderr=subprocess.STDOUT,
                         stdout=subprocess.PIPE)
    p.wait()
    out, err = p.communicate()
    # given that this script is typically run under sudo
    # change the file permissions to the default user
    # to facilitate access
    p = subprocess.Popen(["chown","-R","pi:pi",output_dir],
                         stderr=subprocess.STDOUT,
                         stdout=subprocess.PIPE)
    p.wait()
    out, err = p.communicate()
except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print "Quiting..."  
