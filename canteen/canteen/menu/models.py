from django.db import models
from canteen.foods.models import Food
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _, pgettext_lazy


class MenuType(models.Model):
    """ model class for storing menu type added by admin or coder """
    class Meta:
        db_table = 'menu_type'
        ordering = ['last_updated']

    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, blank=True)


class Menu(models.Model):
    """ base class for storing user order information """
    class Meta:
        db_table = 'food_menu'
        ordering = ['name']

    #TODO move all these to table menu_type,
    #     so admin can add menu_type and we
    #     coder just need to adjust the menu presentation logic,
    #     but not the database.
    #
    #     But the admin got to obey the rule  to add new type?
    # week time
    #Monday = 1
    #Tuesday = 2
    #Wednesday = 3
    #Thursday = 4
    #Friday = 5
    #Saturday = 6
    #Sunday = 7

    #day time
    #Morning = 1
    #Noon = 2
    #Evening = 3

    # set of possible menu in a week
    #MENU_WEEK = (
        #(Monday, _('Monday')),
        #(Tuesday, _('Tuesday')),
        #(Wednesday, _('Wednesday')),
        #(Thursday, _('Thursday')),
        #(Friday, _('Friday')),
        #(Saturday, _('Saturday')),
        #(Sunday, _('Sunday')),
    #)

    #set of possible menu in a day
    #MENU_DAY = (
        #(Morning, _(',Morning')),
        #(Noon, _('Noon')),
        #(Evening, _('Evening')),
    #)

    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)
    menu_type = models.ManyToManyField(MenuType)
    foods = models.ManyToManyField(Food, blank=True)

    def __unicode__(self):
        return str(self.name)
