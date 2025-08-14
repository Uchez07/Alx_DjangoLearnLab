from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomUserCreationForm
from . import views
from .views import (
    ListView, CreateView, DeleteView, UpdateView, DetailView
)

urlpatterns =[
    path('', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('accounts/login/', CustomLoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='blog/base'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.posts, name='posts'),
    path('posts/', ListView.as_view(), name='posts'),
    path('post/<int:pk>/', DetailView.as_view(), name='post-detail'),
    path('post/new/', CreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='post-delete'),
]