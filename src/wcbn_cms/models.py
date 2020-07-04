from django.db import models
from django.utils import timezone
# from wcbn_auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    author = models.CharField(max_length=100)
    featured_image = models.ImageField(upload_to='article_images', null=True)

    # created_by = models.ForeignKey(User)
    # updated_by = models.ForeignKey(User)

    # created_at = models.DateTimeField(default=timezone.now)
    # updated_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
