from django.conf.urls import patterns, url

urlpatterns = patterns(
    'canteen.exercise.views',
    url(r'^$', 'index', {'template_name': 'exercise/index.html'}, 'exercise_index'),
    url(r'detail/(?P<exercise_type>\d+)?$', 'detail', {'template_name': 'exercise/detail.html'}, 'exercise_order_detail'),
)
