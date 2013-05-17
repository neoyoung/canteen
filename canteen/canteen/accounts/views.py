from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
from django.http import HttpResponseRedirect

import time

from canteen.accounts.forms import RegistrationForm


def register(request, template_name="registration/register.html"):
    """ view displaying customer registration form """
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = RegistrationForm(postdata)
        if form.is_valid():
            user = form.save(commit=False)  # new
            user.email = postdata.get('email', '')  # new
            user.save()  # new
            un = postdata.get('username', '')
            pw = postdata.get('password1', '')
            from django.contrib.auth import login, authenticate
            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:
                login(request, new_user)
                url = urlresolvers.reverse('my_account')
                return HttpResponseRedirect(url)
    else:
        form = RegistrationForm()
    page_title = 'User Registration'
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


@login_required
def my_account(request, template_name="registration/my_account.html"):
    """ page displaying user account information,
        past order list and account options """
    page_title = 'My Account'
    name = request.user.username
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

class IpLoginBackend(object):

    # This is called by the standard Django login procedure
    def authenticate(self, username=None, password=None):
        try:
            # Check if the user exists in Django's local database
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            # Create a user in Django's local database
            user = User.objects.create_user(time.time(), username, 'passworddoesntmatter')

        return user

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
