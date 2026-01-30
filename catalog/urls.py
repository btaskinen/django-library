"""Defines URL routes for the catalog application."""
from django.urls import path
from .views import index, BookListView, BookDetailView

urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail')
]
