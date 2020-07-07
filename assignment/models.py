"""
--------------------------------------------------------------------------------------------------
    File Name: ftlabs/ftlabstest/models.py
    Description: This module contains all model definitions that are common across the different
    categories of entities in ftlabs application.
--------------------------------------------------------------------------------------------------
"""

from django.db import models
from datetime import datetime
import dateparser

# Create your models here.


class CustomDateTimeField(models.DateTimeField):
    """
    This function changes the date time format in the model.
    """
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return datetime.now()


class ActivityPeriod(models.Model):
    """
    This modal provides the start and end time of an activity.
    Attributes:
        start_time (DateTimeField, optional): Holds the start time of an activity.
        end_time (DateTimeField, optional): Holds the end time of an activity.
    """
    start_time = CustomDateTimeField(blank=False, null=False, verbose_name="Start Time")
    end_time = CustomDateTimeField(blank=False, null=False, verbose_name="End Time")

    def __str__(self):
        """
          Method that returns the start and end time
        """
        return '{}, {}'.format(self.start_time, self.end_time)

    class Meta:
        db_table = 'activity_period'  # Name of the database table


class User(models.Model):
    """
    This modal provides the details of an user.
    Attributes:
        id (CharField, mandatory, primary_key): Holds the id of an user.
        real_name (CharField, mandatory): Holds the name of an user.
        tz (DateTimeField, mandatory): Holds the timezone of an activity.
        activity_period (ManyToManyField(ActivityPeriod), mandatory): Holds the start and end times of an activity.
    """
    TIMEZONES = (
        ('America/Los_Angeles', 'America/Los_Angeles'),
        ('Asia/Kolkata', 'Asia/Kolkata'),
    )

    id = models.CharField(primary_key=True, max_length=9, blank=False, null=False, verbose_name="User ID")
    real_name = models.CharField(max_length=255, blank=False, null=False, verbose_name="User Name")
    tz = models.CharField(max_length=255, choices=TIMEZONES)
    activity_period = models.ManyToManyField(ActivityPeriod)

    def __str__(self):
        """
          Method that returns the id of each user
        """
        return '{}, {}'.format(self.id, self.real_name)

    class Meta:
        db_table = 'users'  # Name of the database table
