from django.contrib import admin
from canteen.accounts.models import Whitelist


class WhitelistAdmin(admin.ModelAdmin):
    pass
admin.site.register(Whitelist, WhitelistAdmin)
