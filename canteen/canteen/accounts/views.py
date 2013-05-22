from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core import urlresolvers
from django.http import HttpResponseRedirect

from canteen.accounts.models import Whitelist

import time


def my_account(request, template_name="registration/my_account.html"):
    """ page displaying user account information,
        past order list and account options """
    page_title = 'My Account'
    name = request.user.username
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


class IpLoginBackend(object):

    def authenticate(self, user=None):
        return user

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

def ip_not_allowed(request,template_name="ip_not_allowed.html"):
    """
       Request ip not in whitelist,
       find the admin.
    """
    page_title = 'ip_not_allowed'
    return render_to_response(template_name,locals(),
                              context_instance=RequestContext(request))
