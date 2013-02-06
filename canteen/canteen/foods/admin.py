from django.contrib import admin
from canteen.foods.models import Food, Category, FoodReview
from canteen.foods.forms import FoodAdminForm

class FoodAdmin(admin.ModelAdmin):
    form = FoodAdminForm
    # sets values for how the admin site lists your foods
    list_display = ('name', 'created_at', 'updated_at',)
    # which of the fields in 'list_display' tuple link to admin food page
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    #exclude = ('created_at', 'updated_at',)
    readonly_fields = ('created_at', 'updated_at',)
    # sets up slug to be generated from food name
    prepopulated_fields = {'slug' : ('name',)}

# registers your food model with the admin site
admin.site.register(Food, FoodAdmin)

class CategoryAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists categories
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    #exclude = ('created_at', 'updated_at',)
    readonly_fields = ('created_at', 'updated_at',)

    # sets up slug to be generated from category name
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)

class FoodReviewAdmin(admin.ModelAdmin):
    list_display = ('food', 'user', 'title', 'date', 'rating', 'is_approved')
    list_per_page = 20
    list_filter = ('food', 'user', 'is_approved')
    ordering = ['date']
    search_fields = ['user','content','title']

admin.site.register(FoodReview, FoodReviewAdmin)
