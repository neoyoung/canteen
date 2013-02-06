# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.utils import simplejson

#
from canteen.order.models import Order

#import
import time


def testJson(request):
    message = {"fact_type": "", "fact_note": ""}
    if request.is_ajax():
        message['fact_note'] = "wahahahahah"
    else:
        message = "You're the lying type, I can just tell."
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')


def update_order(request, order_id):
    pass


def get_order(request):
    result = {'status': 0, }
    if request.is_ajax():
        orderSet = Order.all.filter(is_active=True, date=dates.today(),
                                    user=request.user)
        if orderInfo:
            result = result.update({'status': 1,
                                    'order_type': orderSet[0].order_type})
        else:
            pass
        json = simplejson.dumps(result)
        return HttpResponse(json, mimetype='application/json')
    else:
        return HttpResponseRedirect('/')
