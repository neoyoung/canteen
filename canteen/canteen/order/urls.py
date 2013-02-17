from django.conf.urls import patterns, url
#from canteen import settings

urlpatterns = patterns(
    'canteen.order.views',
    url(r'^$', 'get_order', {}, 'get_order'),
    url(r'^(?P<order_id>[\d]+)/$',
        'update_order', {}, 'update_order'),
    url(r'^add/$',
        'add_order', {}, 'add_order'),
    url(r'^delete/$', 'delete_order',
        {}, 'delete_order'),
    url(r'^list/$', 'list_order',
        {}, 'list_order'),
)
