from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#class CST(datetime.tzinfo):
    #def utcoffset(self, dt):
        #return datetime.timedelta(hours=+8)

    #def dst(self, dt):
        #return datetime.timedelta(0)


class BaseOrderInfo(models.Model):
    """ base class for storing user order information """
    class Meta:
        abstract = True

    #contact info, just for fun to test the feature =)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)


class OrderType(models.Model):
    """ model class for storing a user order instance """
    class Meta:
        db_table = 'OrderType'
        ordering = ['name']
        verbose_name_plural = 'orderTypes'

    #order info
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.name


class Order(BaseOrderInfo):
    """ model class for storing a user order instance """
    class Meta:
        db_table = 'order'
        ordering = ['date']
        verbose_name_plural = 'orders'

    #TODO move the order type to a standalone table
    # each individual status
    #LUNCH = 1
    #DINNER = 2
    #BOTH = 3

    # set of possible order statuses
    #ORDER_TYPE = (
                 #(LUNCH, 'lunch'),
                 #(DINNER, 'dinner'),
                 #(BOTH, 'both'),
    #)

    #order info
    #date = models.DateTimeField(default=datetime.datetime.now(CST()))
    date = models.DateTimeField(default=timezone.now())
    order_type = models.ForeignKey(OrderType)
    is_active = models.BooleanField(default=True)
    ip_address = models.IPAddressField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return u'Order #' + str(self.id)
