from django.contrib import admin
from canteen.exercise.models import Exercise

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['-updated_at']
    search_fields = ['name', 'description']
    readonly_fields = ('created_at', 'updated_at',)

admin.site.register(Exercise, ExerciseAdmin)

