from django.conf.urls.defaults import *
from canteen import settings

urlpatterns = patterns(
    'canteen.accounts.views',
    (r'^register/$', 'register',
     {'template_name': 'registration/register.html'}, 'register'),
    (r'^my_account/$', 'my_account',
     {'template_name': 'registration/my_account.html'}, 'my_account'),
)
