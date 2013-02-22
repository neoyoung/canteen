from django.conf.urls import patterns, include, url
#from canteen import settings

urlpatterns = patterns(
    'canteen.foods.views',
    url(r'^$', 'index', {'template_name': 'foods/index.html'}, 'foods_index'),
)
