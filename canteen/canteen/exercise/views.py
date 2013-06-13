from datetime import datetime, timedelta, time

from django.shortcuts import  render_to_response
from django.template import RequestContext
from django.utils import timezone

from canteen.exercise.models import Exercise

def index(request, template_name="exercise/index.html"):
    #page init
    startTime = datetime.combine(datetime.now(), time(0, 0, 0, 0))\
            .replace(tzinfo=timezone.get_current_timezone())
    endTime = datetime.combine(datetime.now(), time(23, 59, 59, 99999))\
            .replace(tzinfo=timezone.get_current_timezone())

    #today_excercise = Exercise.objects.filter(offertime_start__gte=startTime,
            #offertime_stop__lte=endTime)
    exercise_list = Exercise.objects.all()
    page_title = 'exercise page'

    return render_to_response(template_name, locals(),
            context_instance=RequestContext(request))


def detail(request, template_name="exercise/detail.html"):
    pass



