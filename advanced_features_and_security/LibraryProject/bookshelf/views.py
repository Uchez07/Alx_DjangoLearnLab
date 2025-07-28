from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    ...
