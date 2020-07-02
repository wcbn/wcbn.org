from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from trix.admin import TrixAdmin
from .models import Article


@admin.register(Article)
class PostAdmin(TrixAdmin, admin.ModelAdmin):
    trix_fields = ('text',)


class FlatPageAdmin(TrixAdmin, FlatPageAdmin):
    trix_fields = ('content',)
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (
                'template_name',
            ),
        }),
    )


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
