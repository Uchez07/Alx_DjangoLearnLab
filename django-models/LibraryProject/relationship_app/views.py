from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile


# Create your views here.
def list_book(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', "Book.objects.all()")

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/signup.html', {'form': form})

def register(request):  # 👈 renamed from signup_view to register
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Role-check functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# relationship_app/views.py (continued)

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'user': request.user})


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'user': request.user})


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'user': request.user})
