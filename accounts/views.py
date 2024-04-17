from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *
from .models import *
# Create your views here
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.shortcuts import render
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            confirm_password = form.cleaned_data['password2']
            if password != confirm_password:
                messages.error(request, "Passwords do not match")
                return render(request, 'signup.html', {'form': form})
            user.set_password(password)  # Use set_password to hash the password
            user.save()
            messages.success(request, "You are registered")
            form = SignupForm()  # Reset the form after successful submission
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
            username=cd['username'],
            password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request,'Authenticated successfully')
                    return redirect(reverse('profile'))
                else:
                    messages.info(request,'Disabled account')
            else:
                messages.error(request,'Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def landing(request):
    return render(request,'landing.html')
