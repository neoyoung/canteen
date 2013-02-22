from django.contrib import admin
from canteen.order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'date', 'user')
    list_filter = ('date',)
    search_fields = ('date',)

    #fieldsets = (
        #('Basics', {'fields': ('status', 'email', 'phone')}),
        #('Shipping', {'fields': ('shipping_name', 'shipping_address_1',
                                 #'shipping_address_2', 'shipping_city',
                                 #'shipping_state',
                                 #'shipping_zip', 'shipping_country')}),
        #('Billing', {'fields':('billing_name', 'billing_address_1',
                #'billing_address_2', 'billing_city','billing_state',
                #'billing_zip', 'billing_country')})
                 #)
admin.site.register(Order, OrderAdmin)
