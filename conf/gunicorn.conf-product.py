#!/usr/bin/env python
# encoding: utf-8
"""
gunicorn.conf.py

Created by <zhkzyth@gmail.com> on  6 09, 2013
"""
import os
LOG_PATH = "/Users/admin/code/canteen/log/"

def numCPUS():
    if not hasattr(os,"sysconf"):
        raise RuntimeError("No sysconf detected.")
    return os.sysconf("SC_NPROCESSORS_ONLN")

user="admin"
workers = numCPUS()*2 + 1
bind = "127.0.0.1:8000"
pidfile = "/tmp/gunicorn-demo.pid"
backlog = 2048
logfile = LOG_PATH + "gunicorn_product.log"
loglevel = "info"
