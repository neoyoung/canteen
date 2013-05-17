from django.conf.urls import patterns, url

urlpatterns = patterns(
    'canteen.foods.views',
    url(r'^$', 'index', {'template_name': 'foods/index.html'}, 'foods_index'),
)
