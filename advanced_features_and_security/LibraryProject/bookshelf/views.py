from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    ...

@login_required
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # replace with your actual success URL
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/example_form.html', {'form': form})