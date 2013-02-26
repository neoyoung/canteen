#!/usr/bin/env python
# encoding: utf-8
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
#
from django.db.models import Q

from datetime import timedelta, datetime, time

from django.db import connection

from canteen.order.models import Order
from canteen.menu.models import Menu, OffertimeType

#help message
_ERROR_MSG = """
    <!DOCTYPE html><html lang="en"><body><h1>%s</h1><p>%%s</p></body></html>
            """
_400_ERROR = _ERROR_MSG % '400 Bad Request'
_403_ERROR = _ERROR_MSG % '403 Forbidden'
_405_ERROR = _ERROR_MSG % '405 Not Allowed'

#TODO be more friendly =)
_LUNCH_OK = 1  # 午餐预定成功
_LUNCH_BOOK_ALREADY = 2  # 午餐已经预定过了
_LUNCH_OVERTIME = 3  # 非午餐预定时间

_DINNER_OK = 4  # 晚餐预定成功
_DINNER_BOOK_ALREADY = 5  # 晚餐已经预定过了
_DINNER_OVERTIME = 6  # 非晚餐预定时间

_TWO_MEALS_OK = 7
_TWO_MEALS_NOT_OK = 8

_DEFAULT_ERROR_CODE = 404  # error unknown

#OFFERTIME_TYPE
_LUNCH_TYPE = 1
_DINNER_TYPE = 2


#helper func
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


class TimeInterface(object):

    def _get_menu(self):
        menu_set = Menu.objects.filter(
            offer_type__offertime_start__lte=datetime.now().time(),
            offer_type__offertime_stop__gt=datetime.now().time(),
            offer_type__offer_type=self.offertime_type)
        if menu_set:
            return menu_set[0]
        else:
            return []

    def _get_timerange(self):
        offer_type_info = OffertimeType.objects.filter(
            offer_type=self.offertime_type)[0]
        start_datetime = offer_type_info.offertime_start
        end_datetime = offer_type_info.offertime_stop

        return (start_datetime, end_datetime)

    #some helper funcs
    def _get_date_range(self):
        start_time, end_time = self._get_timerange()
        start_datetime = datetime.combine(datetime.now(), start_time)
        end_datetime = datetime.combine(start_datetime, end_time)

        return (start_datetime, end_datetime)

    def _is_valid_time(self):
        now = datetime.now().time()
        offer_type = OffertimeType.objects.filter(
            offertime_start__lte=now,
            offertime_stop__gt=now,
            offer_type=self.offertime_type
        )

        if offer_type:
            return True
        else:
            return None

    def _is_book_already(self):
        order = Order.objects.filter(
            date__range=self._get_date_range(),
            menu__offer_type__offer_type=self.offertime_type,
            user=self.request.user)
        return order

    def get_message_type(self):
        return [self.msgType]

    def add_order(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def list_order(self, template_name):
        """ list Morning orders"""
        orderList = Order.objects.filter(
            date__range=self._get_date_range(),
            menu__offer_type__offer_type=self.offertime_type
        )

        return render_to_response(
            template_name, locals(),
            context_instance=RequestContext(self.request))


class LunchTime(TimeInterface):
    def __init__(self, request):
        self.msgType = _LUNCH_OK
        self.offertime_type = _LUNCH_TYPE
        self.request = request

    def add_order(self):

        if self._is_valid_time():
            if not self._is_book_already():
                order_menu = self._get_menu()
                order = Order()
                order.user = self.request.user
                order.date = datetime.now()
                order.menu = order_menu
                order.save()
                return order
            else:
                self.msgType = _LUNCH_BOOK_ALREADY
        else:
            self.msgType = _LUNCH_OVERTIME
        #not valid or no such menu
        return {}


class DinnerTime(TimeInterface):
    def __init__(self, request):
        self.msgType = _DINNER_OK
        self.offertime_type = _DINNER_TYPE
        self.request = request

    def _is_valid_time(self):
        now = datetime.now().time()
        offer_type = OffertimeType.objects.filter(
            offertime_start__lte=now,
            offertime_stop__gt=now,
            offer_type=self.offertime_type
        )

        if offer_type:
            return True
        else:
            return None

    def add_order(self):
        #import pdb
        #pdb.set_trace()
        if self._is_valid_time():
            if not self._is_book_already():
                order_menu = self._get_menu()
                order = Order()
                order.user = self.request.user
                order.date = timezone.now()
                order.menu = order_menu
                order.save()
                return order
            else:
                self.msgType = _DINNER_BOOK_ALREADY
        else:
            self.msgType = _DINNER_OVERTIME
        #not valid or no such menu
        return {}


class TwomealsTime(TimeInterface):

    def __init__(self, request):
        self.msgType = _TWO_MEALS_OK
        self.lunch = LunchTime(request)
        self.dinner = DinnerTime(request)

    def get_message_type(self):
        #import pdb
        #pdb.set_trace()
        if self.msgType == _TWO_MEALS_OK:
            return super(TwomealsTime, self).get_message_type()
        else:
            return [self.lunch.msgType, self.dinner.msgType]

    def add_order(self):
        """
            a helper func to simplify user action.
        """
        #TODO roll back
        self.lunch.add_order()
        self.dinner.add_order()
        if (self.lunch.msgType == _LUNCH_OK
                and self.dinner.msgType == _DINNER_OK):
            return True
        else:
            self.msgType = _TWO_MEALS_NOT_OK
            return []


#@login_required
#@ajax_view(method="POST")
def add_order(request):
    """ Create user order.
        User can create an order one day.
    """
    postdata = request.POST.copy()
    response = {'success': 'False'}
    #TODO check user input
    timeMap = {
        1: LunchTime,
        2: DinnerTime,
        3: TwomealsTime
    }
    currentTime = timeMap[int(postdata['offertime_type'])](request)

    if currentTime.add_order():
        response.update({'msgType': currentTime.get_message_type(),
                         'success': 'True'})
    else:
        response.update({'msgType': currentTime.get_message_type()})

    response = simplejson.dumps(response)

    return HttpResponse(response, mimetype='application/json')


#TODO more friendly
def list_order(request, template_name="orders/index.html"):
               #list_type="lunch"):
    """ list today orders"""
    now = datetime.now()

    forenoon_start = datetime.combine(now, time(0, 0, 0, 0))
    forenoon_end = datetime.combine(now, time(12, 0, 0, 0))

    afternoon_start = datetime.combine(now, time(0, 0, 0, 0))
    afternoon_end = datetime.combine(now, time(23, 59, 59, 99999))

    if forenoon_start <= now <= forenoon_end:
        ##lunch time
        currentTime = LunchTime(request)
    elif afternoon_start <= now <= afternoon_end:
        ##dinner time
        currentTime = DinnerTime(request)
    else:
        currentTime = LunchTime(request)
    return currentTime.list_order(template_name)


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
