#!/usr/bin/env python
# encoding: utf-8
"""
gunicorn.conf.py

Created by <zhkzyth@gmail.com> on  6 09, 2013
"""
import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def numCPUS():
    if not hasattr(os,"sysconf"):
        raise RuntimeError("No sysconf detected.")
    return os.sysconf("SC_NPROCESSORS_ONLN")

user="admin"
workers = numCPUS()*2 + 1
bind = "127.0.0.1:8000"
pidfile = "/tmp/gunicorn-demo.pid"
backlog = 2048
logfile = ROOT_PATH + "/log/gunicorn_demo.log"
loglevel = "info"
