from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomUserCreationForm
from . import views

urlpatterns =[
    path('', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('accounts/login/', CustomLoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='blog/base'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.posts, name='posts'),
]