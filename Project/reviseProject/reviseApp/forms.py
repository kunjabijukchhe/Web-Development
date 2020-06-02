from django import forms
from django.contrib.auth.models import User
from reviseApp.models import UserModel

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email','password','first_name','last_name')

class UserURLForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields=('user_url','user_profile_pic')
