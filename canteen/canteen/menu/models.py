from django.db import models
from canteen.foods.models import Food
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta, tzinfo
from django.utils.translation import ugettext_lazy as _

Hours3 = timedelta(hours=3)


class OffertimeType(models.Model):
    """ model class for storing menu type added by admin or coder """
    class Meta:
        db_table = 'offertime_type'
        ordering = ['last_updated']

    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    show_index = models.IntegerField(
        unique=True, help_text=_("Please input the unique show index"))
    creator = models.ForeignKey(User, blank=True, null=True)
    description = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Menu(models.Model):
    """ base class for storing user order information """
    class Meta:
        db_table = 'menu'
        ordering = ['name']

    #NAMES = (
            #(_('Breakfast'), _('Breakfast')),
            #(_('Lunch'), _('Lunch')),
            #(_('Dinner'), _('Dinner'))
    #)

    name = models.CharField(max_length=50)
    show_name = models.CharField(max_length=50, default=_('lunch'))

    is_active = models.BooleanField(default=True)
    offertime_type = models.ForeignKey(OffertimeType)
    foods = models.ManyToManyField(Food, blank=True)

    #offer time range
    #TODO default delta is 3hours according to the OffertimeType
    #
    _now = timezone.now()
    _now3 = _now + Hours3
    offertime = models.DateTimeField(default=_now)
    offertime_start = models.TimeField(default=_now.time)
    offertime_stop = models.TimeField(default=_now3)

    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
