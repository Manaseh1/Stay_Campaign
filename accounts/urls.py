from django.urls import path
from .views import *
urlpatterns = [
    path('signin',signin,name = 'login'),
    path('signup',signup,name = 'signup'),
    path('',landing,name='landing'),
    
]
