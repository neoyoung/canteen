from django.conf.urls import patterns, url


urlpatterns = patterns(
    'canteen.order.views',
    url(r'^add/$',
        'add_order', {}, 'add_order'),
    url(r'^list/(?P<offertime_type>\d+)*$', 'list_order',
        {"template_name": "orders/index.html"}, 'list_order'),
)
