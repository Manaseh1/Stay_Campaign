from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser


# Create your views here.
# def create(request):
# def create_post(request):

# Assuming user is an existing User instance

# Create a Profile instance for the user


@login_required(login_url='login')
def create_profile(request):
    try:
        profile = request.user.profile
        return redirect(reverse('edit_profile'))
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = EditProfileForm(instance=profile)

    return render(request, 'profile_form.html', {'form': form})

@login_required(login_url='login')
def edit_profile(request):
    try:
        profile = request.user.profile
        
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = EditProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


@login_required(login_url='login')
def create_mangender(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # Handle the case where the user doesn't have a profile
        return HttpResponse("User profile does not exist")
    
    try:
        mangender = profile.mangender
    except Mangender.DoesNotExist:
        mangender = Mangender(user=request.user,profile=request.user.profile)
    if profile.dockets == 'none':
        return redirect('profile')
    
    if request.method == 'POST':
        form = CreateMangender(request.POST, instance=mangender)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CreateMangender(instance=mangender)
    
    context = {'form': form}
    return render(request, 'mangenda.html', context)

class CustomAnonymousUser:
    def __init__(self, username='AnonymousUser'):
        
        self.username = username
        self.profile = None
        # self.comment = Comments(name = self.name,profile = self.profile)

def candidate_profile(request):
    if request.user.is_authenticated:

        try:
            docketchecker = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            docketchecker = None

        user = request.user
        if Mangender.DoesNotExist:
            user_mangender = []

        if Mangender.objects.filter(user=user).exists():
            user_mangender = Mangender.objects.get(user=user)
            return render(request, 'candidate_profile.html', {'user': user,'user_mangender': user_mangender})                         
        return render(request, 'candidate_profile.html', {'user': user,'user_mangender': user_mangender,'docketchecker':docketchecker})                     
    else:
        user = CustomAnonymousUser()
        return render(request, 'candidate_profile.html',{'user':user})

def presidents_list(request):
    presidents = Profile.objects.filter(dockets='president')
    context = {'presidents':presidents}
    return render(request,'presidents.html',context)

def president_detail(request,id):
    president = get_object_or_404(Profile.objects.filter(dockets='president',id=id))
    return render(request,'pres_detail.html',{'president':president})

def vice_list(request):
    vices= Profile.objects.filter(dockets='vice')
    context = {'vices':vices}
    return render(request,'vices.html',context)

def vice_detail(request,id):
    vice = get_object_or_404(Profile.objects.filter(dockets='vice',id=id))
    return render(request,'vice_detail.html',{'vice':vice})

def dockets(request):
    return render(request,'dockets.html')
# Remember not to use keywords


def create_comment(request, id):
    mangenda = get_object_or_404(Mangender, id=id)
    comments = Comments.objects.filter(mangender=mangenda.id)
    form = CommentForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            content = form.cleaned_data['content']
            username = request.user.username if request.user.is_authenticated else 'AnonymousUser'
            Comments.objects.create(mangender=mangenda, name=username, content=content)
            return redirect('comments', id=id)
    else:
        initial_data = {'mangender': mangenda.id, 'name': request.user.username if request.user.is_authenticated else 'AnonymousUser', 'created_at': timezone.now}
        form = CommentForm(initial=initial_data)

    context = {'form': form, 'mangenda': mangenda, 'comments': comments, 'profile': request.user}
    return render(request, 'comments.html', context)

def my_logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        return redirect('profile')
    else:
        return HttpResponse('not sure')
    