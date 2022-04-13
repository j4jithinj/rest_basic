from django.urls import path
from .views import *
from rest_framework import generics
from . import serializers

urlpatterns = [
    path('', userlogin, name='login'),
    path('usersignup', usersignup, name='usersignup'),
    path('userlogin', userlogin, name='userlogin'),
    path('create/superuser/', generics.ListCreateAPIView.as_view(
        serializer_class=serializers.SuperUserSerializer,
        queryset=CustomUser.objects.all()
    ), name='superuser-create')
]
