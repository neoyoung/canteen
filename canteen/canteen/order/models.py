from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from canteen.menu.models import Menu


class BaseOrderInfo(models.Model):
    """ base class for storing user order information """
    class Meta:
        abstract = True

    #contact info, just for fun to test the feature =)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)


class Order(BaseOrderInfo):
    """ model class for storing a user order instance """
    #order info
    date = models.DateTimeField(default=timezone.now())
    menu = models.ForeignKey(Menu)
    is_active = models.BooleanField(default=True)
    ip_address = models.IPAddressField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)


    class Meta:
        db_table = 'order'
        ordering = ['date']
        verbose_name_plural = 'orders'


    def __unicode__(self):
        return u'Order #' + str(self.id)
