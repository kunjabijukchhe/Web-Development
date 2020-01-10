from django.shortcuts import render
#from .forms import NewUserFrom
from appform import views
from . import forms
# Create your views here.

def index(request):
    return render(request,'home.html')


def form_name(request):
    form=forms.formName()


    if request.method=='POST':
        form=forms.formName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("Name:"+form.cleaned_data['name'])
            print("Email:"+form.cleaned_data['email'])
            print("Text:"+form.cleaned_data['text'])
            print("password:"+form.cleaned_data['password'])
    return render(request,'form.html',{'form':form})
# def users(request):
#     form = NewUserFrom()
#
#     if request.method == "POST":
#         form = NewUserFrom(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print('ERROR FORM INVALID')
#
#     return render(request,'form.html',{'form':form})
