from django import forms
from app.models import User,UserPass

class newUser(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

class newUserPass(forms.ModelForm):
    class Meta:
        widgets={'password':forms.PasswordInput}
        model=UserPass
        fields='__all__'
