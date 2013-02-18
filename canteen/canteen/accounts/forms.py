from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext, ugettext_lazy as _

#from ecomstore.accounts.models import UserProfile

#class UserProfileForm(forms.ModelForm):
    #class Meta:
        #model = UserProfile
        #exclude = ('user',)


class RegistrationForm(UserCreationForm):
    """ subclass of Django's UserCreationForm, to handle customer registration
        with a required minimum length
        and password strength. Also contains an additional field for
        capturing the email on registration.
    """
    password1 = forms.RegexField(
        label=_("Password"), regex=r'^(?=.*\W+).*$',
        help_text=_(
            'Password must be six characters long and contain \
            at least one non-alphanumeric character.'),
        widget=forms.PasswordInput, min_length=6)
    password2 = forms.RegexField(label=_("Password confirmation"),
                                 regex=r'^(?=.*\W+).*$',
                                 widget=forms.PasswordInput, min_length=6)
    email = forms.EmailField(max_length="50", label=_("Email"))
