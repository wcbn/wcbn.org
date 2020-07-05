from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    author = models.CharField(max_length=100)
    featured_image = models.ImageField(upload_to='article_images', null=True, blank=True)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=140)
    summary = models.TextField()
    featured_image = models.ImageField(upload_to='event_images', null=True, blank=True)

    start_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    location_name = models.CharField(max_length=140, null=True, blank=True)
    location_address = models.CharField(max_length=140, null=True, blank=True)

    url = models.URLField(max_length=140, null=True, blank=True)
    age_restriction = models.CharField(max_length=20, null=True, blank=True)
    presented_by_wcbn = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Concert(models.Model):
    title = models.CharField(max_length=140)
    summary = models.TextField()
    featured_image = models.ImageField(upload_to='concert_images', null=True, blank=True)

    start_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    door_time = models.TimeField(null=True, blank=True)

    end_date = models.DateField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    location_name = models.CharField(max_length=140, null=True, blank=True)
    location_address = models.CharField(max_length=140, null=True, blank=True)

    url = models.URLField(max_length=140, null=True, blank=True)
    age_restriction = models.CharField(max_length=20, null=True, blank=True)
    presented_by_wcbn = models.BooleanField(default=False)

    def __str__(self):
        return self.title
