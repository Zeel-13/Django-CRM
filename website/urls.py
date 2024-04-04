from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('logout/',logout_user,name='logout'),
    path('register/',register_user,name='register'),
    path('record/<int:pk>/',record,name='record'),
]
