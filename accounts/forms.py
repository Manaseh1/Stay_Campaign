from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class LoginForm(forms.Form):
    username =  forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

 

# class LoginForm(forms.Form):
#     username =  forms.CharField( required=True)
#     password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email','password1', 'password2']
    