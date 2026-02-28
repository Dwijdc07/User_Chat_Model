
from django.contrib import admin
from django.urls import path, include
from .views import message



urlpatterns = [
    path('message/',message,name="message")
]
