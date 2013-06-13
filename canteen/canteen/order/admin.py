from django.contrib import admin
from canteen.order.models import MenuOrder,ExerciseOrder


class MenuOrderAdmin(admin.ModelAdmin):
    pass

class ExerciseOrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(MenuOrder, MenuOrderAdmin)
admin.site.register(ExerciseOrder, ExerciseOrderAdmin)
