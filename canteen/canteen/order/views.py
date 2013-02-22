# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse,\
    HttpResponseNotAllowed, HttpResponseForbidden, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.utils import simplejson, timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
#
from django.utils.safestring import mark_safe
from django.utils.decorators import available_attrs
from functools import wraps

from datetime import timedelta, datetime, time

from canteen.order.models import Order
from canteen.menu.models import Menu

#help message
_ERROR_MSG = """
    <!DOCTYPE html><html lang="en"><body><h1>%s</h1><p>%%s</p></body></html>
            """
_400_ERROR = _ERROR_MSG % '400 Bad Request'
_403_ERROR = _ERROR_MSG % '403 Forbidden'
_405_ERROR = _ERROR_MSG % '405 Not Allowed'


#helper func
def timerange(*args, **kwargs):
    start_date = datetime.combine(timezone.now().date(), time(0, 0, 0, 0,
                                  timezone.get_current_timezone()))
    end_date = datetime.combine(start_date, time(23, 59, 59, 999999,
                                timezone.get_current_timezone()))
    return (start_date, end_date)


def get_menu(offertime_type):
    menu_set = Menu.objects.filter(offertime__range=timerange(),
                                   offertime_type__show_index=offertime_type)
    if menu_set:
        return menu_set[0]
    else:
        return None


#def ajax_required(function=None):
    #""" user must post the data via ajax"""
    #def wrapped(request, *args, **kwargs):
        ##import pdb
        ##pdb.set_trace()
        #if request.is_ajax and request.user.is_authenticated():
            #return function(request, *args, **kwargs)
        #else:
            #response = simplejson.dumps({'success': 'false'})
            #return HttpResponse(response, mimetype='application/json')
    #return wrapped

#ajax decorator
def ajax_view(function=None, FormClass=None, method="GET", login_required=True,
              ajax_required=True, json_form_errors=False):
    """
    usage:
        @ajax_view
        def foo():

    or
        @ajax_view(option)
        def foo():
    """
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _ajax_view(request, *args, **kwargs):
            if request.method != method and method != 'REQUEST':
                return HttpResponseNotAllowed(
                    mark_safe(_405_ERROR % ("Request must be a %s." % method)))
            if ajax_required and not request.is_ajax():
                return HttpResponseForbidden(
                    mark_safe(_403_ERROR % "Request must be set via AJAX."))
            if login_required and not request.user.is_authenticated():
                return HttpResponseForbidden(
                    mark_safe(_403_ERROR % "Login required"))

            if FormClass:
                f = FormClass(getattr(request, method))

                if not f.is_valid():
                    if json_form_errors:
                        errors = dict((k, [unicode(x) for x in v])
                                      for k, v in f.errors.items())
                        return HttpResponse(
                            simplejson.dumps(
                                {'error': 'form', 'errors': errors}),
                            'application/json'
                        )
                    else:
                        return HttpResponseBadRequest(
                            mark_safe(
                                _400_ERROR % (
                                    'Invalid form<br />' + f.errors.as_ul()
                                )
                            )
                        )
                request.form = f
            return view_func(request, *args, **kwargs)
        return _ajax_view

    if function:
        return decorator(function)
    return decorator


#u....drop again...Bye~
#@login_required
@ajax_view(method="POST")
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
        order.order_type = postdata['offertime_type']
        order.save()
    else:
        #create a new one?
        response.update({'success': 'False'})

    response = simplejson.dumps(response)
    return HttpResponse(response, mimetype='application/json')


#@login_required
@ajax_view(method="POST")
def add_order(request):
    """ create user order.
        User can create an order one day.
    """
    postdata = request.POST.copy()
    #print postdata
    response = {'success': 'False'}

    start_date, end_date = timerange()

    orderSet = Order.objects.filter(date__range=(start_date, end_date),
                                    user=request.user)
    if orderSet:
        #exit one ,just update it
        over_time = check_overtime()

        if over_time:
            response.update({'msgType': over_time.type})
        else:
            response.update({'msgType': over_time.type})

        #return update_order(request)

    else:
        #add one!
        order_menu = get_menu(postdata['offertime_type'])
        if order_menu:
            order = Order()
            order.user = request.user
            order.date = timezone.now()
            order.menu = order_menu
            order.save()
            #update the order_menu table
            response.update({'success': 'True'})
        else:
            pass

    response = simplejson.dumps(response)
    return HttpResponse(response, mimetype='application/json')


@ajax_view()
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


#just disable this feature.
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


def list_order(request, template_name="orders/index.html"):
    """ list today orders"""
    start_date = timezone.now().date()
    end_date = start_date + timedelta(days=1)
    orderList = Order.objects.filter(date__range=(start_date, end_date))

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
