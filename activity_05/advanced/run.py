#!/usr/bin/python
# coding: utf-8
""" Filename:     run.py
    Descritpion:  This file runs the Flask application service
    Requirements: Flask
    Author:       MakerBro
"""
from webapp.application import app

if __name__ == '__main__':
    app.run(debug=True)
