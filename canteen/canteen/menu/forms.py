from django import forms
from canteen.menu.models import Menu, OffertimeType


#TODO extend the form to simply interactions
class MenuAdminForm(forms.ModelForm):
    """ ModelForm class to validate food instance data
        before saving from admin interface """
    class Meta:
        model = Menu
