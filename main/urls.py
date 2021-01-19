from django.contrib import admin
from django.urls import path
from .views import  index
from django.conf import settings

urlpatterns = [
    path('', index,name="index"),

]
