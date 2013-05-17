from django.contrib import admin
from canteen.foods.models import Food, Category, FoodReview
from canteen.foods.forms import FoodAdminForm


class FoodAdmin(admin.ModelAdmin):
    form = FoodAdminForm
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['-created_at']
    search_fields = ['name', 'description',
                     'meta_keywords', 'meta_description']
    readonly_fields = ('created_at', 'updated_at',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description',
                     'meta_keywords', 'meta_description']
    readonly_fields = ('created_at', 'updated_at',)

    # sets up slug to be generated from category name
    prepopulated_fields = {'slug': ('name',)}


class FoodReviewAdmin(admin.ModelAdmin):
    list_display = ('food', 'user', 'title', 'date', 'rating', 'is_approved')
    list_per_page = 20
    list_filter = ('food', 'user', 'is_approved')
    ordering = ['date']
    search_fields = ['user', 'content', 'title']


admin.site.register(Food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodReview, FoodReviewAdmin)
