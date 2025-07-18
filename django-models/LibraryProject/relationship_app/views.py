from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library


# Create your views here.
def list_book(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', "Book.objects.all()")

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
