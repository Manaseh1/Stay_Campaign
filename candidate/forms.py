from .models import *
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
    
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class CreateMangender(forms.ModelForm):
    class Meta:
        model = Mangender
        fields = '__all__'
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
        