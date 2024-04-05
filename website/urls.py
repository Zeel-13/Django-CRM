from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('logout/',logout_user,name='logout'),
    path('register/',register_user,name='register'),
    path('record/<int:pk>/',record,name='record'),
    path('delete_record/<int:pk>/',delete_record,name='delete_record'),
    path('add_record/',add_record,name='add_record'),
]
