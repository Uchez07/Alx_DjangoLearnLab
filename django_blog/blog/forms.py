from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # No 'author', we'll set that automatically

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 20:
            raise forms.ValidationError("Content must be at least 20 characters long.")
        return content

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...',
                'rows': 3
            })
        }
        labels = {
            'content': ''
        }
        def clean_content(self):
            content = self.cleaned_data.get('content')
            if not content.strip():
                raise forms.ValidationError("Comment cannot be empty.")
            if len(content) < 3:
                raise forms.ValidationError("Comment must be at least 3 characters long.")
            return content
