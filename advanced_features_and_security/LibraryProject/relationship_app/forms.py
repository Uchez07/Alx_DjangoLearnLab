from django import forms
from .models import Book  # Ensure Book exists in models.py

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
