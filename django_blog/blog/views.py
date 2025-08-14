from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log them in immediately after registration
            return render('base')  # Replace 'home' with your homepage URL name
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login view (Django built-in)
class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

# Logout view (Django built-in)
class CustomLogoutView(LogoutView):
    next_page = 'base'  # Redirect after logout

def base(request):
    return render(request, 'blog/base.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')  # Reload the page after saving
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

@login_required
def posts(request):
    # Example posts list
    post_list = [
        {"title": "First Post", "content": "This is the first post."},
        {"title": "Second Post", "content": "This is the second post."},
    ]
    return render(request, "blog/posts.html", {"posts": post_list})