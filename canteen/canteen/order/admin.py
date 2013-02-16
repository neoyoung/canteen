from django.contrib import admin
from canteen.order.models import Order


#class OrderItemInline(admin.StackedInline):
    #model = OrderItem
    #extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'date', 'order_type', 'user')
    list_filter = ('date', 'order_type')
    search_fields = ('date',)
    #inlines = [OrderItemInline, ]

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