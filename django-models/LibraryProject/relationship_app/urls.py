from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_all_books_view, name='book_list'), 
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
]