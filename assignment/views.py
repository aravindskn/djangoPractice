"""
--------------------------------------------------------------------------------------------------
    File Name: ftlabs/ftlabstest/views.py
    Description: This module contains all view definitions that are common across the different
    categories of entities in ftlabs application.
--------------------------------------------------------------------------------------------------
"""
from rest_framework.generics import ListAPIView
from .models import (User, ActivityPeriod)
from .serializers import (ActivityPeriodSerializer, UserSerializer)
from rest_framework.response import Response

# Create your views here.


class UserListView(ListAPIView):
    """
        This module contains the definitions for LIST and CREATE method.
        This module lists and creates zero or more Users.
    """
    lookup_field = 'id'
    serializer_class = UserSerializer

    # Custom List definition for showing data in custom json.
    def list(self, request, *args, **kwargs):
        response = super(UserListView, self).list(request, args, kwargs)
        newResponse = {"ok": True, "members": []}
        for key, value in newResponse.items():
            if key == "members":
                newResponse[key] = response.data
        return Response(newResponse)

    def get_queryset(self):
        return User.objects.all()


class ActivityPeriodListView(ListAPIView):
    """
        This module contains the definitions for LIST and CREATE method.
        This module lists and creates zero or more Activity Period.
    """
    lookup_field = 'id'
    serializer_class = ActivityPeriodSerializer

    def get_queryset(self):
        return ActivityPeriod.objects.all()
