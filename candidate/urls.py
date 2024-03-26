from django.urls import path
from .views import *
urlpatterns = [
    path('',candidate_profile,name = 'profile'),
    path('create/',create_profile,name = 'create_profile'),
    path('edit/',edit_profile,name = 'edit_profile'),
    
]