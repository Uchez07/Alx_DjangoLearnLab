from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.list_all_books_view, name='book_list'), 
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),  # formerly signup_view
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('admin-only/', views.admin_view, name='admin_view'),
    path('librarian-only/', views.librarian_view, name='librarian_view'),
    path('member-only/', views.member_view, name='member_view'),

]