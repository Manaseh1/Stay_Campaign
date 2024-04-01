from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponse

# Create your views here.
# def create(request):
# def create_post(request):

# Assuming user is an existing User instance

# Create a Profile instance for the user

@login_required
def create_profile(request):
    try:
        profile = request.user.profile
        return redirect(reverse('edit_profile'))  # Redirect to edit_profile if profile exists
    except Profile.DoesNotExist:
        pass

    form = ProfileForm(request.POST,request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponse('Successfully saved')
            # return redirect('profile')
    return render(request, 'profile_form.html', {'form': form})


@login_required
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
@login_required
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
    
    if request.method == 'POST':
        form = CreateMangender(request.POST, instance=mangender)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CreateMangender(instance=mangender)
    
    context = {'form': form}
    return render(request, 'mangenda.html', context)

                  
def candidate_profile(request):
    # profile = get_object_or_404(Profile,pk=request.user.pk)
    return render(request,'candidate_profile.html')