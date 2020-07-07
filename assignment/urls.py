"""
--------------------------------------------------------------------------------------------------
    File Name: ftlabs/ftlabstest/urls.py
    Description: This module contains all API endpoints for the ftlabstest application.
--------------------------------------------------------------------------------------------------
"""

from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view()),  # List Users
    path('activity/', views.ActivityPeriodListView.as_view()),  # List Activity Period
]
