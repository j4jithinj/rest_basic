import imp
from unicodedata import name
from django.urls import path 
from .views import *

urlpatterns = [ 
    path('', userlogin, name='login'),
    path('usersignup', usersignup, name='usersignup'),
    path('userlogin', userlogin, name='userlogin'),
]