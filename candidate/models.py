from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    class Dockets(models.TextChoices):
        president = 'president','president'
        vice = 'vice','vice'
        none = 'none','none'
    user = models.OneToOneField(User,on_delete = models.CASCADE,null=True)
    about_me = models.TextField(blank = True)
    dockets = models.CharField(max_length=10,choices =Dockets.choices,default = Dockets.none)
    image = models.ImageField(blank = True,null = True)
    # docket = models.CharField(max_length =100)
    def __str__(self):
        return self.user.username

class Mangender(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,null=True)
    profile = models.OneToOneField(Profile, on_delete = models.CASCADE,null=True)
    title = models.CharField(max_length = 255, blank = True)
    manifesto = models.TextField(blank = True)
    agenda = models.TextField(blank = True)
    
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    mangender = models.ForeignKey(Mangender, on_delete = models.CASCADE,null=True)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE,null = True,blank=True)
    name = models.CharField(max_length=80)
    content = models.TextField(max_length=100,blank = True,default= None)
    created_at = models.DateTimeField(default = timezone.now) 
    class Meta:
        ordering =['-created_at']