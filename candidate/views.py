from django.shortcuts import render

# Create your views here.
def candidate_profile(request):
    return render(request,'candidate_profile.html')