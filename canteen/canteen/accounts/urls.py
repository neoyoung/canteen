from django.conf.urls.defaults import *
from canteen import settings

urlpatterns = patterns(
    'canteen.accounts.views',
    (r'^my_account/$', 'my_account',
     {'template_name': 'registration/my_account.html'}, 'my_account'),
    (r'^ipnotallowed/$', 'ip_not_allowed',{},'ip_not_allowed'),
)
