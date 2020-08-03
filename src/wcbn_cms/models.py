from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from wcbn_util.models import TimeStampedModel
from wcbn_util.fields import CharField


class Article(TimeStampedModel):
    title = CharField()
    text = models.TextField()
    author = CharField(default='WCBN Staff', blank=True)
    featured_image = models.ImageField(upload_to='article_images')
    featured_image_caption = CharField()
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "articles"


class Event(TimeStampedModel):
    title = CharField()
    summary = models.TextField()
    featured_image = models.ImageField(upload_to='event_images', null=True, blank=True)
    featured_image_caption = CharField(null=True, blank=True)

    start_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    location_name = CharField(null=True, blank=True)
    location_address = CharField(null=True, blank=True)

    url = models.URLField("URL", null=True, blank=True)
    age_restriction = CharField(null=True, blank=True)
    is_presented_by_wcbn = models.BooleanField("Presented by WCBN?", default=False)
    is_free = models.BooleanField("Free?", default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "events"


class Concert(TimeStampedModel):
    title = CharField()
    summary = models.TextField()
    featured_image = models.ImageField(upload_to='concert_images', null=True, blank=True)
    featured_image_caption = CharField(null=True, blank=True)

    start_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    door_time = models.TimeField(null=True, blank=True)

    end_date = models.DateField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    location_name = CharField(null=True, blank=True)
    location_address = CharField(null=True, blank=True)

    url = models.URLField("URL", null=True, blank=True)
    age_restriction = CharField(null=True, blank=True)
    is_presented_by_wcbn = models.BooleanField("Presented by WCBN?", default=False)
    is_free = models.BooleanField("Free?", default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "concerts"
    
    def clean(self):
        if self.featured_image and not self.featured_image_caption:
            raise ValidationError("Featured Image Caption required for Featured Image")
        if not self.featured_image and self.featured_image_caption:
            raise ValidationError("Featured Image required for Featured Image Caption")
