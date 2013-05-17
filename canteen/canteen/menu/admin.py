from django.contrib import admin
from canteen.menu.models import Menu, OffertimeType
from canteen.menu.forms import MenuAdminForm


class MenuAdmin(admin.ModelAdmin):
    form = MenuAdminForm
    list_display = ('name', 'last_updated',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['-last_updated']
    search_fields = ['name']
    filter_vertical = ('foods',)

admin.site.register(Menu, MenuAdmin)


class OffertimeTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(OffertimeType, OffertimeTypeAdmin)
