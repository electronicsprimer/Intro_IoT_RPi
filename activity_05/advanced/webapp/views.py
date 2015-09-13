#!/usr/bin/python
# coding: utf-8
""" 
    Filename:     views.py
    Description:  This file is one of the views file that can contain the
                  routes for the application
    Requirements: 
    Author:       MakerBro
"""
import os
import csv
import json
import flask
from application import app
from settings import APP_STATIC, APP_DATA

# importing application wide parameters and global variables that have been
# defined in application.py
message = app.config['HELLO_WORLD']

@app.route('/')
def webapp():
    return flask.render_template('main.html', data=message)
