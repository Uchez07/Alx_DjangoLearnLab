from django.shortcuts import render, redirect
from django.contrib.auth import Login
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log them in immediately after registration
            return redirect('home')  # Replace 'home' with your homepage URL name
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login view (Django built-in)
class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

# Logout view (Django built-in)
class CustomLogoutView(LogoutView):
    next_page = 'home'  # Redirect after logout

def home(request):
    return redirect(request, 'blog/base.html')
