from django.shortcuts import render
from appform import forms
# Create your views here.

def index(request):
    return render(request,'home.html')


def form_name(request):
    form=forms.formName()

    if request.method=='POST':
        form=forms.formName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print('Name:'+form.cleaned_data['name'])
            print('Email:'+form.cleaned_data['email'])
            print('Text:'+form.cleaned_data['text'])

    return render(request,'form.html',{'form':form})
