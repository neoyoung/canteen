# -*- coding: utf-8 -*-
from datetime import datetime

from django.utils import timezone
from django.shortcuts import  render_to_response
from django.template import RequestContext
from django.views.generic import list_detail

from canteen.exercise.models import Exercise
from canteen.order.models import ExerciseOrder
from canteen.common.utils import is_number

def index(request, template_name="exercise/index.html"):
    #page init
    exercise_list = Exercise.objects.all()
    page_title = 'exercise page'

    return render_to_response(template_name, locals(),
            context_instance=RequestContext(request))

def detail(request, exercise_type='',template_name="exercise/detail.html"):

    def _get_timerange():
        exercise = Exercise.objects.filter(
                id=request.POST.get("exercise_type"))[0]
        start_datetime = exercise.offertime_start
        end_datetime = exercise.offertime_stop

        return (start_datetime, end_datetime)

    def _is_book_already():
        order = ExerciseOrder.objects.filter(
                user=request.user,
                exercise__id=request.POST.get('exercise_type'),
                date__range=_get_timerange(),
                )
        if order:
            return True
        else:
            return False

    def _is_valid_time():

        now_time = datetime.now().replace(tzinfo=timezone.get_current_timezone())

        exercise = Exercise.objects.filter(
                offertime_start__lte=now_time,
                offertime_stop__gte=now_time,
                id=request.POST.get('exercise_type'),
                )

        if exercise:
            return True
        else:
            return None

    if request.method == "POST":
        exercise_type = request.POST.get('exercise_type','')
        notice_arr = {
                'success':('报名成功啦，看看有谁也一起去的~','success'),
                'error':('报名出问题了，联系前台先记着报名吧','error'),
                'warning':('现在不是报名时间哦','block'),
                'info':("woops...你已经报过名了...",'info'),
                }
        if exercise_type is None or not is_number(exercise_type):
            notice = notice_arr['error']

        exercise_order_list = ExerciseOrder.objects.filter(id=exercise_type)

        if not _is_valid_time():
            notice = notice_arr['warning']
        elif _is_book_already():
            notice = notice_arr['info']
        else:
            exercise = Exercise.objects.filter(id=exercise_type)
            if not exercise:
                notice = notice_arr['error']
            else:
                try:
                    order = ExerciseOrder()
                    order.user = request.user
                    order.date = datetime.now()
                    order.exercise = exercise[0]
                    order.save()
                    notice = notice_arr['success']
                except:
                    notice = notice_arr['error']
    else:
        notice = None
        exercise_order_list = ExerciseOrder.objects.filter(id=exercise_type)

    return render_to_response(template_name, locals(),
            context_instance=RequestContext(request))
