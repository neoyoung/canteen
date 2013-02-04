from django.conf.urls import patterns, include, url
import settings

urlpatterns = patterns('canteen.foods.views',
      url(r'^$','index', {'template_name': 'foods/index.html'}, 'foods_index'),
      url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category',
         {'template_name': 'foods/category.html'}, 'catalog_category'),
      url(r'^product/(?P<product_slug>[-\w]+)/$', 'show_product',
         {'template_name': 'foods/food.html'}, 'foods_food'),
      url(r'^tag_cloud/$', 'tag_cloud',
         {'template_name': 'foods/tag_cloud.html'}, 'tag_cloud'),
      url(r'^tag/(?P<tag>[-\w]+)/$', 'tag',
         {'template_name': 'foods/tag.html'}, 'tag'),
      url(r'^review/food/add/$', 'add_review', {}, 'add_food_review'),
      url(r'^tag/food/add/$', 'add_tag'),
)



