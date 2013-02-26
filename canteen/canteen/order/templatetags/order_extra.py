#!/usr/bin/python
# vim: set fileencoding=UTF-8 :
from django import template

register = template.Library()


@register.filter()
def switchType(value):
    #import pdb
    #pdb.set_trace()
    typeMap = {1: "午餐", 2: "晚餐"}

    try:
        order_type = typeMap[value]
    except:
        order_type = "午餐"

    return order_type
