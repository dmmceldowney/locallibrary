from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre # imports relevant model classes we'll see in the views

from django.views import generic


# Create your views here.
def index(request):
    """View function for the home page of site"""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default
    num_authors = Author.objects.count()

    # context for rendering the HTML
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

    
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    #context_object_name = 'my_book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    #template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location


class BookDetailView(generic.DetailView):
    model = Book


class AuthorsListView(generic.ListView):
    model = Author
    paginate = 50


class AuthorDetailView(generic.DetailView):
    model = Author