#encoding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse,\
    HttpResponseNotAllowed, HttpResponseForbidden, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.utils.decorators import available_attrs
from django.utils import simplejson, timezone
from django.db.models import Q

from functools import wraps
from datetime import timedelta, datetime, time

from canteen.order.models import Order
from canteen.menu.models import Menu, OffertimeType

#help message
_ERROR_MSG = """
    <!DOCTYPE html><html lang="en"><body><h1>%s</h1><p>%%s</p></body></html>
            """
_400_ERROR = _ERROR_MSG % '400 Bad Request'
_403_ERROR = _ERROR_MSG % '403 Forbidden'
_405_ERROR = _ERROR_MSG % '405 Not Allowed'


#ajax helper func
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


class Offertype(object):

    def __init__(self, user, offertime_type):
        self.offertime_type = offertime_type
        self.user = user
        self.message = None
        self.menu = None

    def _get_menu(self):
        if self.menu is not None:
            return self.menu
        else:
            menu = Menu.objects.filter(
                offer_type__offer_type=self.offertime_type)[0]
            if menu:
                self.menu = menu
                return menu
            else:
                return []

    def _get_timerange(self):
        offer_type_info = OffertimeType.objects.filter(
            offer_type=self.offertime_type)[0]
        start_datetime = offer_type_info.offertime_start
        end_datetime = offer_type_info.offertime_stop

        return (start_datetime, end_datetime)

    def _get_date_range(self):
        start_time, end_time = self._get_timerange()
        start_datetime = datetime.combine(datetime.now(), start_time)\
            .replace(tzinfo=timezone.get_current_timezone())
        end_datetime = datetime.combine(start_datetime, end_time)\
            .replace(tzinfo=timezone.get_current_timezone())

        return (start_datetime, end_datetime)

    def _is_valid_time(self):
        now_time = datetime.time(
            datetime.now().replace(tzinfo=timezone.get_current_timezone())
        )
        offer_type = OffertimeType.objects.filter(
            offertime_start__lte=now_time,
            offertime_stop__gt=now_time,
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
            user=self.user)
        return order

    def get_message(self):
        return self.message

    def _set_message(self, content):
        self.message = self._get_menu().name.encode('utf-8') + content

    #TODO seperate the error message ????
    def add_order(self):
        if self._is_valid_time():
            order_menu = self._get_menu()
            if not self._is_book_already():
                order = Order()
                order.user = self.user
                order.date = datetime.now()
                order.menu = order_menu
                order.save()
                self._set_message("预定成功拉。")
                return order
            else:
                self._set_message("已经预定过拉。")
        else:
            self._set_message("不在预定时间里哦。")
        #not valid or no such menu
        return {}


@ajax_view(method="POST")
def add_order(request):
    """ Create user order."""
    messages = []
    postdata = request.POST.copy()

    for offertime_type in postdata.getlist("offertime_type[]"):
        offer_type = Offertype(request.user, int(offertime_type))
        offer_type.add_order()
        messages.append(offer_type.get_message())

    response = simplejson.dumps({'messageArr': messages})

    return HttpResponse(response, mimetype='application/json')


def list_order(request, template_name, offertime_type):
    """ list today orders"""
    today_start = datetime.combine(
        datetime.now(), time(0, 0, 0, 0))\
        .replace(tzinfo=timezone.get_current_timezone())

    default_show = False

    if offertime_type is None:
        offertime_type = OffertimeType.objects\
            .filter(is_active=True).order_by("offer_type")[0].offer_type
        default_show = True

    order_list = Order.objects.filter(
        date__gte=today_start, is_active=True,
        menu__offer_type__offer_type=offertime_type)

    offer_type_list = OffertimeType.objects.filter(is_active=True)\
        .order_by("offer_type")

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
