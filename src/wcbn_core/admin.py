from django.contrib import admin
from django.contrib.sites.models import Site

admin.site.site_header = 'wcbn administration'
admin.site.index_title = 'Freeing your mind, managing your content etc.'

admin.site.unregister(Site)
