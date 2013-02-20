# -*- coding: utf-8 -*-
from django.db import models
from django.http import Http404
from canteen import settings
from django.contrib.auth.models import User
import tagging


#keep this for future extension
class ActiveCategoryManager(models.Manager):
    """ Manager class to return only those categories
        where each instance is active """
    def get_query_set(self):
        return super(ActiveCategoryManager,
                     self).get_query_set().filter(is_active=True)


class Category(models.Model):
    """ model class containing information about a category  """
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text='Unique value for food page URL,\
                   created automatically from name.')
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField(
        max_length=255,
        help_text='Comma-delimited set of SEO keywords for keywords meta tag',
        blank=True)
    meta_description = models.CharField(
        max_length=255,
        help_text='Content for description meta tag',
        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    active = ActiveCategoryManager()

    class Meta:
        db_table = 'categories'
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), {'category_slug': self.slug})

    #@property
    #def cache_key(self):
        #return self.get_absolute_url()


class ActiveFoodManager(models.Manager):
    """ Manager class to return only
        those foods where each instance is active """
    def get_query_set(self):
        return super(ActiveFoodManager, self).get_query_set()\
            .filter(is_active=True)


class Food(models.Model):
    """ model class containing information about a food """
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        help_text='Unique value for food page URL,\
                   created automatically from name.')
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField(blank=True, default=1)
    description = models.TextField(blank=True)
    meta_keywords = models.CharField(
        "Meta Keywords",
        max_length=255,
        help_text='Comma-delimited set of SEO keywords for keywords meta tag',
        blank=True)
    meta_description = models.CharField(
        "Meta Description",
        max_length=255,
        help_text='Content for description meta tag',
        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #time_at = models.DateField(auto_now=True, editable=True)
    categories = models.ManyToManyField(Category, blank=True)

    # image fields require a varchar(100) in db
    image = models.ImageField(upload_to='images/foods/main', blank=True)
    thumbnail = models.ImageField(
        upload_to='images/foods/thumbnails',
        blank=True)
    image_caption = models.CharField(max_length=200, blank=True)

    objects = models.Manager()
    active = ActiveFoodManager()

    class Meta:
        db_table = 'food'
        ordering = ['-created_at']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog_food', (), {'food_slug': self.slug})

try:
    tagging.register(Food)
except tagging.AlreadyRegistered:
    pass


class ActiveFoodReviewManager(models.Manager):
    """ Manager class to return only those food
        reviews where each instance is approved """
    def all(self):
        return super(ActiveFoodReviewManager, self).all()\
                                                   .filter(is_approved=True)


class FoodReview(models.Model):
    """ model class containing food review
        data associated with a food instance """
    RATINGS = ((5, 5), (4, 4), (3, 3), (2, 2), (1, 1),)

    food = models.ForeignKey(Food)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=5, choices=RATINGS)
    is_approved = models.BooleanField(default=True)
    content = models.TextField()

    objects = models.Manager()
    approved = ActiveFoodReviewManager()

    class Meta():
        db_table = 'food_review'
        ordering = ['-date']
