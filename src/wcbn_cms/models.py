from django.db import models
from django.utils import timezone
# from wcbn_auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    author = models.CharField(max_length=100)

    # created_by = models.ForeignKey(User)
    # updated_by = models.ForeignKey(User)

    # created_at = models.DateTimeField(default=timezone.now)
    # updated_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# class Event(models.Model):
#     title = models.CharField(max_length=140)
#     description = models.TextField()

#     start_date = models.DateField()
#     start_time = models.TimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#     end_time = models.TimeField(null=True, blank=True)

#     location_name = models.CharField(max_length=140, null=True, blank=True)
#     location_address = models.CharField(max_length=140, null=True, blank=True)

#     url = models.CharField(max_length=140, null=True, blank=True)
#     age_restriction = models.CharField(max_length=50, null=True, blank=True)
#     presented_by = models.CharField(max_length=140, null=True, blank=True)
#     door_time = models.TimeField(null=True, blank=True)

