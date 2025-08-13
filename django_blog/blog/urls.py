from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomUserCreationForm
from . import views

urlpatterns =[
    path('', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view, name='login'),
    path('logout/', CustomLogoutView.as_view, name='login'),
    path('profile/', views.profile, name='profile'),
]