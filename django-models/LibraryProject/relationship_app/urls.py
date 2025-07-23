from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib import admin
from .views import LibraryDetailView, register
from .views import home_view,add_book_view, edit_book_view, delete_book_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('books/', views.list_book, name='book_list'), 
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),  # formerly signup_view
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('admin-only/', views.admin_view, name='admin_view'),
    path('librarian-only/', views.librarian_view, name='librarian_view'),
    path('member-only/', views.member_view, name='member_view'),
    path('books/add/', add_book_view, name='book_add'),
    path('books/<int:pk>/edit/', edit_book_view, name='book_edit'),
    path('books/<int:pk>/delete/', delete_book_view, name='book_delete'),

]