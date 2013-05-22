#TODO add the union user rec web service.
from django.db import models
from django.contrib.auth.models import User

class Whitelist(models.Model):
    """ model class containing information about a category  """
    ip = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    is_active = models.BooleanField(default=True)


    class Meta:
        db_table = 'whitelist'
        ordering = ['ip']

    def __unicode__(self):
        return self.ip
