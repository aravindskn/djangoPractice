"""
--------------------------------------------------------------------------------------------------
    File Name: ftlabs/ftlabstest/admin.py
    Description: This module contains all the models that are added in the django admin page.
--------------------------------------------------------------------------------------------------
"""

from django.contrib import admin
from .models import User, ActivityPeriod

# Register your models here.

admin.site.register(User)  # User Model Admin Registration
admin.site.register(ActivityPeriod)  # Activity Period Admin Registration


class UserAdmin(admin.ModelAdmin):
    """
    List of Attributes of User Model to show in Admin
    """
    list_display = ('id', 'real_name', 'tz', 'activity_period')


class ActivityPeriodAdmin(admin.ModelAdmin):
    """
    List of Attributes of Activity Period Model to show in Admin
    """
    list_display = ('start_time', 'end_time')
