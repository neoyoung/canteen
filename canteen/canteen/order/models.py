from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from canteen.menu.models import Menu
from canteen.exercise.models import Exercise

class BaseOrderInfo(models.Model):
    """ base class for storing user order information """
    class Meta:
        abstract = True

    #contact info, just for fun to test the feature =)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    date = models.DateTimeField(default=timezone.now())
    is_active = models.BooleanField(default=True)
    ip_address = models.IPAddressField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)


class MenuOrder(BaseOrderInfo):
    #order info for menu
    menu = models.ForeignKey(Menu)

    class Meta:
        db_table = 'menu_order'
        ordering = ['date']
        verbose_name_plural = 'menu_orders'


    def __unicode__(self):
        return u'Order #' + str(self.id)

class ExerciseOrder(BaseOrderInfo):
    """
        order class for exercise.
    """
    exercise = models.ForeignKey(Exercise)

    class Meta:
        db_table = 'exercise_order'
        ordering = ['date']
        verbose_name_plural = 'exercise_orders'

