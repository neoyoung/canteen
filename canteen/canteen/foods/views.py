#TODO to be implemented

from django.shortcuts import render_to_response
from django.template import RequestContext

from canteen.menu.models import Menu, OffertimeType
from canteen.common.utils import get_today_time_range


def index(request, template_name="foods/index.html"):
    """ site home page """
    #page init
    startTime, endTime =  get_today_time_range()
    today_menu = Menu.objects.filter(offertime__gte=startTime,
                                     offertime__lte=endTime)\
                             .order_by('offer_type__show_index')
    typelist = OffertimeType.objects.filter(is_active=True)

    page_title = '175game canteen'

    return render_to_response(template_name, locals(),
                            context_instance=RequestContext(request))
