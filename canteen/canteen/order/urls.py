from django.conf.urls import patterns, url
#from canteen import settings

urlpatterns = patterns(
    'canteen.order.views',
    url(r'^$', 'get_order', {}, 'get_order'),
    url(r'^order/(?P<order_id>[\d]+)/$',
        'update_order', {}, 'update_order'),
    url(r'test/', 'testJson', {}, 'testJson'),
    url(r'get_order/', 'get_order', {}, 'test'),

)
