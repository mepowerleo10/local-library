from django.shortcuts import render
from django.http.request import HttpRequest
from django.views.generic import ListView, DetailView

from .models import Author, Book, BookInstance, Genre, Language


def index(request: HttpRequest):
    """View function for the home page of the site"""

    # Generate count for some of the main objecs
    num_authors = Author.objects.count()
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact="a")

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_instances": num_instances,
        "num_instances_avalable": num_instances_available,
    }

    # Render a HTML document with the template index.html
    # and the data in the context variable
    return render(request, "index.html", context=context)


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"

    def get_queryset(self):
        # Return the first five books
        return Book.objects.all()[:5]


class BookDetailView(DetailView):
    model = Book
