from django.urls import path
from .views import *
urlpatterns = [
    path('',candidate_profile,name = 'profile'),
    path('create/',create_profile,name = 'create_profile'),
    path('edit/',edit_profile,name = 'edit_profile'),
    path('mangender/',create_mangender,name='create_mangender'),
    path('comments/',create_comment,name='create_comment'),
    path('my_logout/', my_logout, name='logout'), #dont use keywords to name paths
]