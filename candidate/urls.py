from django.urls import path
from .views import *
urlpatterns = [
    path('',candidate_profile,name = 'profile'),
    path('create/',create_profile,name = 'create_profile'),
    path('edit/',edit_profile,name = 'edit_profile'),
    path('mangender/',create_mangender,name='create_mangender'),
    path('comments/<int:id>',create_comment,name='comments'),
    path('my_logout/', my_logout, name='logout'), #dont use keywords to name paths
    path('dockets/',dockets,name='dockets'),
    path('presidents-list/',presidents_list,name='presidents-list'),
    path('president-detail/<int:id>',president_detail,name='president_detail'),
    path('vice-list/',vice_list,name='vice-list'),   
    path('vice-detail/<int:id>',vice_detail,name='vice_detail'),
    
    
]