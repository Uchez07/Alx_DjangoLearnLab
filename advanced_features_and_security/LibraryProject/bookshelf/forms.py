from django import forms
from .models import Book  # assuming you're using the Book model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']  # adjust to your actual model fields
