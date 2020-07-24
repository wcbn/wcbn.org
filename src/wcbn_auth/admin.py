from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User
from django.utils.translation import gettext, gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    ordering = ('date_joined',)
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')
    fieldsets = (
        (None, {
            "fields": (
                'first_name',
                'last_name',
                'email',
                'password',
                'is_active',
                'is_staff',
                'is_superuser'
            ),
        }),
    )

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
