"""Admin site configuration for the catalog application."""

from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    """Customizes the Django admin interface for Author objects."""
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    """Customizes the Django admin interface for Book objects."""
    list_display = ('title', 'authors', 'display_genre')

admin.site.register(Genre)

@admin.register(BookInstance)
class AdminBookInstance(admin.ModelAdmin):
    """Customizes the Django admin interface for BookInstance objects."""
    list_filter = ('status', 'due_back')

admin.site.register(Language)
