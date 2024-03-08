from django.urls import path
from .views import *
urlpatterns = [
    path('',candidate_profile,name = 'profile')
]