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


#@login_required
#@ajax_required
def update_order(request, order_id):
    """ update user order """
    postdata = request.POST.copy()
    response = {'success': 'True'}

    #is_active = postdata.active
    #time_at   = postdata.time_at

    order_type = postdata.type
    today = datetime.date.today()

    #update
    orderSet = Order.objects.filter(date__year=today.year,
                                    date__month=today.month,
                                    date__day=today.day,
                                    user=request.user)

    if orderSet:
        order = orderSet[0]
        order.order_type = order_type
        order.save()
        #response.update({""})
    else:
        #create a new one?
        response.update({'success': 'False'})

    response = simplejson.dumps(response)
    return HttpResponse(response, mimetype='application/json')


#@login_required
#@ajax_required
def add_order(request):
    """ create user order """
    postdata = request.POST.copy()
    response = {'success': 'True'}

    #is_active = postdata.active
    #time_at   = postdata.time_at

    order_type = postdata.order_type
    today = datetime.date.today()

    #update
    orderSet = Order.objects.filter(date__year=today.year,
                                    date__month=today.month,
                                    date__day=today.day,
                                    user=request.user)

    if orderSet:
        #exit one ,just update it
        update_order(request)
    else:
        #add one!
        order = Order()
        order.order_type = order_type
        order.user = request.user
        #order.ip_address =

        response.update({'success': 'False'})

    response = simplejson.dumps(response)
    return HttpResponse(response, mimetype='application/json')


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
