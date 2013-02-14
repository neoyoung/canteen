from django.conf.urls import patterns, url
#from canteen import settings

urlpatterns = patterns(
    'canteen.order.views',
    url(r'^$', 'get_order', {}, 'get_order'),
    url(r'^(?P<order_id>[\d]+)/$',
        'update_order', {}, 'update_order'),
    url(r'^add/$',
        'add_order', {}, 'add_order'),
)
