from django.contrib import admin
from trix.admin import TrixAdmin
from .models import Article


@admin.register(Article)
class PostAdmin(TrixAdmin, admin.ModelAdmin):
    trix_fields = ('text',)
