# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils import simplejson
#python lib
from datetime import *
#third plugin
import tagging
from tagging.models import Tag, TaggedItem
#
from canteen.foods.models import Category, Food
from canteen.menu.models import Menu


def index(request, template_name="foods/index.html"):
    """ site home page """
    #search_recs = stats.recommended_from_search(request)
    #featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)
    #view_recs = stats.recommended_from_views(request)

    startTime = datetime.combine(timezone.now().date(), time(0, 0, 0, 0,
                                 timezone.get_current_timezone()))
    endTime = datetime.combine(startTime, time(23, 59, 59, 999999,
                               timezone.get_current_timezone()))

    today_menu = Menu.objects.filter(offertime__gte=startTime,
                                     offertime__lte=endTime)\
                             .order_by('offertime_type__show_index')


    page_title = '175game canteen'

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
