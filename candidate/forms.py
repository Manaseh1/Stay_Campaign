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