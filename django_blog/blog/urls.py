from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomUserCreationForm
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns =[
    path('', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('accounts/login/', CustomLoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='blog/base'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.posts, name='posts'),
    
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    
]