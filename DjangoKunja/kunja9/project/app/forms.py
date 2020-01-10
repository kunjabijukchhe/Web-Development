from django import forms
from app.models import User

class NewUserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields='__all__'
