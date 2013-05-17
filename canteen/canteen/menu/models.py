from datetime import datetime, timedelta, tzinfo

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from canteen.foods.models import Food


class OffertimeType(models.Model):
    """ model class for storing menu type added by admin or coder """
    class Meta:
        db_table = 'offertime_type'
        ordering = ['last_updated']

    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    #TODO seperate the show and type
    show_index = models.IntegerField(
        unique=True, help_text=_("Please input the unique show index"))
    offer_type = models.IntegerField(
        unique=True, help_text=_("Please input the unique index number"))
    creator = models.ForeignKey(User, blank=True, null=True)
    description = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    #offer time range
    #TODO default delta is 3hours according to the OffertimeType
    offertime_start = models.TimeField()
    offertime_stop = models.TimeField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('canteen.order.views.list_order', args=[int(self.offer_type)])


class Menu(models.Model):
    """ base class for storing user order information """
    class Meta:
        db_table = 'menu'
        ordering = ['name']

    name = models.CharField(max_length=50)
    show_name = models.CharField(max_length=50, default=_('lunch'))

    is_active = models.BooleanField(default=True)
    offer_type = models.ForeignKey(OffertimeType)
    foods = models.ManyToManyField(Food, blank=True)

    _now = timezone.now()
    offertime = models.DateTimeField(default=_now)

    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
