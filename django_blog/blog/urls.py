from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomUserCreationForm

urlpatterns =[
    path('', name, name='base'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view, name='login'),
    path('logout/', CustomLogoutView.as_view, name='login'),
]