from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from membership.forms import DefaultUserRegisterForm


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
        form = DefaultUserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='User')
            user.groups.add(group)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')

    else:
        form = DefaultUserRegisterForm()

    return render(request, 'membership/register.html', {'form': form})


def register_moderator_view(request):
    if request.method == "POST":
        form = DefaultUserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Moderator')
            user.groups.add(group)
            login(request, user)
            messages.success(request, "You have registered successfully as a Moderator.")
            return redirect('home')

    else:
        form = DefaultUserRegisterForm()

    return render(request, 'membership/register.html', {'form': form})