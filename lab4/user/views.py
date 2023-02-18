from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.forms import MainUserCreateForm


def home(request):
    print('rofl')
    return render(request, 'home.html')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = MainUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            # Redirect to a success page
            return redirect('home')
    else:
        form = MainUserCreateForm()
    return render(request, 'register.html', {'form': form})


# @login_required

def logout_user(request):
    logout(request)
    return redirect('home')
