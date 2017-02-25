from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from .forms import *


def signup(request):
    if request.user.is_authenticated():
        return redirect('upload')
    else:
        form = SignupForm()
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                #user = form.save(commit = False)
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                new_password = form.cleaned_data['password']
                user = User(username=username, email= email)
                user.set_password(new_password)
                user.save()
                auth.login(request,user)
                return redirect('upload')
            return render(request, 'signup.html', {'form':form})
        return render(request, 'signup.html', {'form':form})


def login(request):
    if request.user.is_authenticated():
        return redirect('upload')
    else:
        form = LoginForm()
        if request.method =='POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(username = username, password=password)
                if user is not None and user.is_active:
                    print user
                    auth.login(request,user)
                    return redirect('upload')
                else:
                    return render(request, 'login.html', {'form':form})
            return render(request, 'login.html', {'form':form})
        return render(request, 'login.html', {'form':form})


def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
        return redirect('login')
    else:
        return redirect('login')