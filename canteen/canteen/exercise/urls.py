from django.conf.urls import patterns, url

urlpatterns = patterns(
    'canteen.exercise.views',
    url(r'^$', 'index', {'template_name': 'exercise/index.html'}, 'exercise_index'),
)
