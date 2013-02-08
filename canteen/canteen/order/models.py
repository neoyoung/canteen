from django.db import models
#from django import forms
from django.contrib.auth.models import User
#from canteen.foods.models import Food
#import decimal


class BaseOrderInfo(models.Model):
    """ base class for storing user order information """
    class Meta:
        abstract = True

    #contact info
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    #shipping information
    #shipping_name = models.CharField(max_length=50)
    #shipping_address_1 = models.CharField(max_length=50)
    #shipping_address_2 = models.CharField(max_length=50, blank=True)
    #shipping_city = models.CharField(max_length=50)
    #shipping_state = models.CharField(max_length=2)
    #shipping_country = models.CharField(max_length=50)
    #shipping_zip = models.CharField(max_length=10)

    #billing information
    #billing_name = models.CharField(max_length=50)
    #billing_address_1 = models.CharField(max_length=50)
    #billing_address_2 = models.CharField(max_length=50, blank=True)
    #billing_city = models.CharField(max_length=50)
    #billing_state = models.CharField(max_length=2)
    #billing_country = models.CharField(max_length=50)
    #billing_zip = models.CharField(max_length=10)


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
    date = models.DateTimeField()
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
