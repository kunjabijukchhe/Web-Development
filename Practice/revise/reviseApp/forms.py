from django import forms
from reviseApp.models import Record

class NewRecord(forms.ModelForm):
    class Meta:
        model=Record
        fields='__all__'
