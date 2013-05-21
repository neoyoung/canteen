#TODO add the union user rec web service.
from django.db import models


class Whitelist(models.Model):
    """ model class containing information about a category  """
    user_name = models.CharField(max_length=50)
    ip = models.CharField(blank=True, default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'whitelist'
        ordering = ['user_name']

    def __unicode__(self):
        return self.user_name
