from django import forms
from app.models import User,Website

class NewUser(forms.ModelForm):
    class Meta:
        model=Website

        widgets={'password':forms.PasswordInput()}
        fields='__all__'
class NewFirstUser(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
