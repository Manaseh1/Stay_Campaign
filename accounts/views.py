from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *
from .models import *
# Create your views here

def signup(request):
    form = SignupForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            email = cd['email']
            password = cd['password1']
            confirm_password = cd['password2']
            if password != confirm_password:
                messages.error(request, "Passwords do not match")
                return render(request, 'signup.html', {'form': form})
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists')
            else:
                messages.success(request, "You are registered")
                form.save()
                form = SignupForm()  # Reset the form after successful submission
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'],password = cd['password'])
            if user is not None :
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Authentication failed')
            else:
                return HttpResponse('Invalid credentials') 
        else:
            form = LoginForm()
    context ={
        'form':form,
    }           
    return render(request, 'login.html',context)

