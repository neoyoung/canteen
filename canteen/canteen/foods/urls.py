from django.conf.urls import patterns, include, url
#from canteen import settings

urlpatterns = patterns(
    'canteen.foods.views',
    url(r'^$', 'index', {'template_name': 'foods/index.html'}, 'foods_index'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category',
        {'template_name': 'foods/category.html'}, 'show_category'),
    url(r'^food/(?P<food_slug>[-\w]+)/$', 'show_food',
        {'template_name': 'foods/food.html'}, 'show_food'),
    url(r'^tag_cloud/$', 'tag_cloud',
        {'template_name': 'foods/tag_cloud.html'}, 'tag_cloud'),
    url(r'^tag/(?P<tag>[-\w]+)/$', 'tag',
        {'template_name': 'foods/tag.html'}, 'tag'),
    url(r'^review/food/add/$', 'add_review', {}, 'add_food_review'),
    url(r'^tag/food/add/$', 'add_tag'),
)
