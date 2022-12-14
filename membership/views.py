from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm


def login_user_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in.')
            return redirect('login')
    return render(request, 'membership/login.html', {})


def logout_user_view(request):
    logout(request)
    messages.success(request, 'You logged out successfully.')
    return render(request, 'membership/logout.html', {})


def register_user_view(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            # login
            login(request, user)

            # get username

            messages.success(request, f'Welcome {user.first_name}!')

            # redirect to homepage
            return redirect('home')

    else:
        form = RegisterUserForm()

    return render(request, 'membership/register.html', {'form': form})
