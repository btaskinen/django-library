"""Admin site configuration for the catalog application."""

from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)
