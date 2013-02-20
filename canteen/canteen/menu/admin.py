from django.contrib import admin
from canteen.menu.models import Menu, MenuType
from canteen.menu.forms import MenuAdminForm


class MenuAdmin(admin.ModelAdmin):
    form = MenuAdminForm
    # sets values for how the admin site lists your menus
    list_display = ('name', 'last_updated',)
    # which of the fields in 'list_display' tuple link to admin menu  page
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['-last_updated']
    search_fields = ['name']

# registers your menu model with the admin site
admin.site.register(Menu, MenuAdmin)


class MenuTypeAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists menuType
    list_display = ('name', 'last_updated', 'creator')
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['-last_updated']
    search_fields = ['name', 'creator']
    #exclude = ('created_at', 'updated_at',)

admin.site.register(MenuType, MenuTypeAdmin)
