from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_all_books_view, name='book_list'), 
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),  # formerly signup_view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]