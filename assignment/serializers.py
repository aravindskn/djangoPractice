"""
--------------------------------------------------------------------------------------------------
    File Name: ftlabs/ftlabstest/serializers.py
    Description: This module contains all serializer definitions that are common across the different
    categories of entities in ftlabs application.
--------------------------------------------------------------------------------------------------
"""

from rest_framework import serializers
from .models import User, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    """
     This is the Serializer for Activity Period Model.
    """

    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


class UserSerializer(serializers.ModelSerializer):
    """
     This is the Serializer for User Model.
    """
    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_period']
        depth = 1
