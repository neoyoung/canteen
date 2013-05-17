from django.contrib import admin
from canteen.order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'date', 'user')
    list_filter = ('date',)
    search_fields = ('date',)

admin.site.register(Order, OrderAdmin)
