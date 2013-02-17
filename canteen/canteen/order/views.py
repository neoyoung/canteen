# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.utils import simplejson, timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


from datetime import timedelta
import datetime

from canteen.order.models import Order


@login_required
#@ajax_required
def update_order(request, order_id=''):
    """ update user order """
    postdata = request.POST.copy()
    response = {'success': 'True'}

    start_date = timezone.now().date()
    end_date = start_date + timedelta(days=1)
    orderSet = Order.objects.filter(date__range=(start_date, end_date),
                                    user=request.user)

    #time range
    if orderSet:
        order = orderSet[0]
        order.order_type = postdata['order_type']
        order.save()
    else:
        #create a new one?
        response.update({'success': 'False'})

    response = simplejson.dumps(response)
    return HttpResponse(response, mimetype='application/json')


@login_required
#@ajax_required
#@csrf_exempt
def add_order(request):
    """ create user order.
        User can create an order one day.
    """
    postdata = request.POST.copy()
    #print postdata
    response = {'success': 'False'}

    start_date = timezone.now().date()
    end_date = start_date + timedelta(days=1)
    orderSet = Order.objects.filter(date__range=(start_date, end_date),
                                    user=request.user)
    if orderSet:
        #exit one ,just update it
        return update_order(request)
    else:
        #add one!
        order = Order()
        order.order_type = postdata['order_type']
        order.user = request.user
        #tmp hack the ip_address
        order.ip_address = ''
        order.save()

        response.update({'success': 'True'})

    response = simplejson.dumps(response)
    return HttpResponse(response, mimetype='application/json')


def get_order(request):
    """ get user's today order"""
    result = {'success': 'False'}

    if request.is_ajax():
        start_date = timezone.now().date()
        end_date = start_date + timedelta(days=1)
        orderSet = Order.objects.filter(date__range=(start_date, end_date),
                                        user=request.user)

        #print orderSet
        if orderSet:
            result.update({'success': 'True',
                           'order_type': orderSet[0].order_type})
        result = simplejson.dumps(result)
        return HttpResponse(result, mimetype='application/json')
    else:
        return HttpResponseRedirect('/')


def delete_order(request):
    response = {'success': 'True'}

    start_date = timezone.now().date()
    end_date = start_date + timedelta(days=1)
    orderSet = Order.objects.filter(date__range=(start_date, end_date),
                                    user=request.user)

    if orderSet:
        #exit one ,just update it
        orderSet[0].delete()
    else:
        response.update({'success': 'False', 'msg': 'item not exit'})

    response = simplejson.dumps(response)
    return HttpResponse(response, mimetype='application/json')


#TODO be good
def ajax_required(request, fn):
    """ a ajax request helper as a decoractor """
    pass


def list_order(request, template_name="orders/index.html"):
    """ list today orders"""
    start_date = timezone.now().date()
    end_date = start_date + timedelta(days=1)
    orderList = Order.objects.filter(date__range=(start_date, end_date))

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
