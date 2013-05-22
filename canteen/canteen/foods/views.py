#TODO to be implemented
from datetime import datetime, timedelta, time

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.template.loader import render_to_string

from canteen.menu.models import Menu, OffertimeType


def index(request, template_name="foods/index.html"):
    """ site home page """
    #page init
    startTime = datetime.combine(datetime.now(), time(0, 0, 0, 0))\
        .replace(tzinfo=timezone.get_current_timezone())
    endTime = datetime.combine(datetime.now(), time(23, 59, 59, 99999))\
        .replace(tzinfo=timezone.get_current_timezone())

    today_menu = Menu.objects.filter(offertime__gte=startTime,
                                     offertime__lte=endTime)\
                             .order_by('offer_type__show_index')
    typelist = OffertimeType.objects.filter(is_active=True)

    page_title = '175game canteen'

    return render_to_response(template_name, locals(),
                            context_instance=RequestContext(request))
