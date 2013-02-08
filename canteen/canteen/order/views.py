# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.utils import simplejson, timezone

#
from canteen.order.models import Order

#import
import time
import datetime


def testJson(request):
    message = {"fact_type": "", "fact_note": ""}
    if request.is_ajax():
        message['fact_note'] = "wahahahahah"
    else:
        message = "You're the lying type, I can just tell."
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')


#@login_required
#@ajax_required
def update_order(request, order_id):
    """ update user order """
    result = {'status': 0, }

    today = datetime.date.


#@login_required
#@ajax_required
def create_order(request):
    """ create the order today """
    result = {'status': 0, }


def get_order(request):
    """ get order of today """
    result = {'status': 0, }
    #today = time.localtime()[2]
    #print timezone.is_aware(datetime.datetime.now())
    #print timezone.get_current_timezone_name()

    today = datetime.date.today()

    if request.is_ajax():
        orderSet = Order.objects.filter(is_active=True,
                                        date__year=today.year,
                                        date__month=today.month,
                                        date__day=today.day,
                                        user=request.user)
        #print orderSet
        if orderSet:
            result.update({'status': 1,
                           'order_type': orderSet[0].order_type})
        json = simplejson.dumps(result)
        return HttpResponse(json, mimetype='application/json')
    else:
        return HttpResponseRedirect('/')


def ajax_required(request, fn):
    """ a ajax request helper as a decoractor """
    pass
