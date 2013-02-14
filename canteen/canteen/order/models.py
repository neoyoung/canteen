from django.db import models
#from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
#from canteen.foods.models import Food
#import decimal
#import time
#import datetime


#class CST(datetime.tzinfo):
    #def utcoffset(self, dt):
        #return datetime.timedelta(hours=+8)

    #def dst(self, dt):
        #return datetime.timedelta(0)


class BaseOrderInfo(models.Model):
    """ base class for storing user order information """
    class Meta:
        abstract = True

    #contact info
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)


class Order(BaseOrderInfo):
    """ model class for storing a user order instance """
    class Meta:
        db_table = 'order'
        ordering = ['date']
        verbose_name_plural = 'orders'

    # each individual status
    LUNCH = 1
    DINNER = 2
    BOTH = 3

    # set of possible order statuses
    ORDER_TYPE = (
                 (LUNCH, 'lunch'),
                 (DINNER, 'dinner'),
                 (BOTH, 'both'),
    )

    #order info
    #date = models.DateTimeField(default=datetime.datetime.now(CST()))
    date = models.DateTimeField(default=timezone.now())
    order_type = models.IntegerField(choices=ORDER_TYPE, default=BOTH)
    is_active = models.BooleanField(default=True)
    ip_address = models.IPAddressField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return u'Order #' + str(self.id)

    #@property
    #def total(self):
        #total = decimal.Decimal('0.00')
        #order_items = OrderItem.objects.filter(order=self)
        #for item in order_items:
            #total += item.total
        #return total

    #@models.permalink
    #def get_absolute_url(self):
        #return ('order_details', (), { 'order_id': self.id })

#class OrderItem(models.Model):
    #""" model class for storing each Product instance purchased in each
        #order """
    #product = models.ForeignKey(Product)
    #quantity = models.IntegerField(default=1)
    #price = models.DecimalField(max_digits=9,decimal_places=2)
    #order = models.ForeignKey(Order)

    #@property
    #def total(self):
        #return self.quantity * self.price

    #@property
    #def name(self):
        #return self.product.name

    #@property
    #def sku(self):
        #return self.product.sku

    #def __unicode__(self):
        #return self.product.name + ' (' + self.product.sku + ')'

    #def get_absolute_url(self):
        #return self.product.get_absolute_url()
