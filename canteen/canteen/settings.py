#!/usr/bin/env python
# encoding: utf-8

from socket import gethostname

production_hosts = ['frebsd_9.0-195']
hostname = gethostname()

if hostname not in production_hosts:
    from debug_settings import *
else:
    from product_settings import *
