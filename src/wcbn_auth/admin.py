from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User

class UserAdmin(BaseUserAdmin):
    ordering = ('date_joined',)
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
