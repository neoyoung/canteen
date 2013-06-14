from datetime import datetime, time

from django.utils import timezone


def get_today_time_range():
    startTime = datetime.combine(datetime.now(), time(0, 0, 0, 0))\
            .replace(tzinfo=timezone.get_current_timezone())
    endTime = datetime.combine(datetime.now(), time(23, 59, 59, 99999))\
            .replace(tzinfo=timezone.get_current_timezone())

    return startTime,endTime

def get_now_date():
    return datetime.now().date()
