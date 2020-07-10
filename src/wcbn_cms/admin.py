from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.db import models
from django.forms import widgets
from trix.admin import TrixAdmin
from .models import Article, Event, Concert, ExecMember, BoardMember, Department, DepartmentMembership


@admin.register(Article)
class ArticleAdmin(TrixAdmin, admin.ModelAdmin):
    trix_fields = ('text',)


@admin.register(Event)
class EventAdmin(TrixAdmin, admin.ModelAdmin):
    trix_fields = ('summary',)
    formfield_overrides = {
        models.TimeField: {'widget': widgets.TimeInput(attrs={'type': 'time'})}
    }


@admin.register(Concert)
class ConcertAdmin(TrixAdmin, admin.ModelAdmin):
    trix_fields = ('summary',)
    formfield_overrides = {
        models.TimeField: {'widget': widgets.TimeInput(attrs={'type': 'time'})}
    }


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

admin.site.register(ExecMember)
admin.site.register(BoardMember)


class DeptMemberInline(admin.TabularInline):
    model = DepartmentMembership
    extra = 0


class DepartmentAdmin(admin.ModelAdmin):
    inlines = [
        DeptMemberInline
    ]


admin.site.register(Department, DepartmentAdmin)
