from django.urls import path
from .views import *
urlpatterns = [
    path('signin',signin,name = 'login'),
    path('',signup,name = 'signup')
]
