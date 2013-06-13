from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        help_text='Unique value for exercise page URL,\
                   created automatically from name.')
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    meta_description = models.CharField(
        "Meta Description",
        max_length=255,
        help_text='Content for description meta tag',
        blank=True)
    offertime_start = models.DateTimeField()
    offertime_stop = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # image fields require a varchar(100) in db
    image = models.ImageField(upload_to='images/exercise/main', blank=True)
    objects = models.Manager()

    class Meta:
        db_table = 'activity'
        ordering = ['-updated_at']

    def __unicode__(self):
        return self.name
