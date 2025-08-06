# views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
import datetime

# List and Create Books
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can create

    def perform_create(self, serializer):
        # Custom logic before saving
        if serializer.validated_data['publication_year'] > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        
        serializer.save()  # Save book

    def create(self, request, *args, **kwargs):
        # Override create to add custom response
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Book created successfully",
            "data": response.data
        }, status=status.HTTP_201_CREATED)

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Ensure no future publication year
        if serializer.validated_data['publication_year'] > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        
        serializer.save()

    def update(self, request, *args, **kwargs):
        # Add custom success message
        response = super().update(request, *args, **kwargs)
        return Response({
            "message": "Book updated successfully",
            "data": response.data
        }, status=status.HTTP_200_OK)

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']


