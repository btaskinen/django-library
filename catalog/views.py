"""Views for the catalog application"""
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import RenewBookForm
from .models import Book, Author, BookInstance

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The all() is implied by default
    num_authors = Author.objects.count()

    num_non_fiction = Book.objects.filter(genre__name='Non-Fiction').count()
    num_fiction = Book.objects.exclude(genre__name="Non-Fiction").count()

    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_non_fiction': num_non_fiction,
        'num_fiction': num_fiction,
        'num_visits': num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    """Class to generate view for list of books.
    The generic list view will query the database to get
    all Book records then render a template"""
    model = Book
    paginate_by = 5

class BookDetailView(generic.DetailView):
    """Class to generate detail views of books."""
    model = Book

class AuthorListView(generic.ListView):
    """Class to generate view for list of authors"""
    model = Author
    paginate_by = 5

class AuthorDetailView(generic.DetailView):
    """Class to generate detail views of authors"""
    model = Author

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 5

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )

class AllLoanedBooksListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing all books currently on loan"""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 5

    def get_queryset(self):
        return (BookInstance.objects.filter(status__exact='o').order_by('due_back'))

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    """View that handles book-loan renewal by librarians"""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':
        form = RenewBookForm(request.POST)

        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()
            return HttpResponseRedirect(reverse('loaned-books'))

    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)

        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)
