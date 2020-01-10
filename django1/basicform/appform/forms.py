from django import forms
from django.core import validators
# def check_for_z(value):
#     if value[0].lower()!='z':
#         raise forms.ValidationError("Name needs to starts with z")

class formName(forms.Form):
    name=forms.CharField()#CharField(validators=[check_for_z])

    email=forms.EmailField()
    verify_email=forms.EmailField(label="Enter your email again!")

    text=forms.CharField(widget=forms.Textarea)

    password=forms.CharField(widget=forms.PasswordInput)
    verify_pass=forms.CharField(widget=forms.PasswordInput,label="Enter your password Again!")

    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        password=all_clean_data['password']
        verify_email=all_clean_data['verify_email']
        verify_pass=all_clean_data['verify_pass']
        if email!=verify_email and password!=verify_pass:
            raise forms.ValidationError("Make sure email and password are match!")




    # def clean_botcatcher(self): # validators=[validators.MaxLengthValidator(0)]
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError('Gotcha Bot!')
    #     return botcatcher

# from django import forms
# from appform.models import User
#
# class NewUserFrom(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
