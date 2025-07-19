from django.urls import path
from .views import LibraryDetailView
from .views import list_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')), 
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]