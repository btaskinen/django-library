"""Admin site configuration for the catalog application."""

from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

class BookInline(admin.TabularInline):
    """tabular inline class for books"""
    model = Book
    extra = 0

@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    """Customizes the Django admin interface for Author objects."""
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BookInline]

class BookInstanceInline(admin.TabularInline):
    """tabular inline class for book instances"""
    model = BookInstance
    extra = 0
@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    """Customizes the Django admin interface for Book objects."""
    list_display = ('title', 'authors', 'display_genre')

    inlines = [BookInstanceInline]

admin.site.register(Genre)

@admin.register(BookInstance)
class AdminBookInstance(admin.ModelAdmin):
    """Customizes the Django admin interface for BookInstance objects."""
    list_display = ('book', 'status', 'due_back', 'id', 'borrower')

    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )

admin.site.register(Language)
