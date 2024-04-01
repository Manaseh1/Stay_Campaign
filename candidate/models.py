from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,null=True)
    about_me = models.TextField(blank = True)
    image = models.ImageField(upload_to='uploads/profile/',blank = True,null = True)
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