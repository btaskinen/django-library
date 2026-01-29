"""Defines URL routes for the catalog application."""
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index')
]
