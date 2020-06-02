from django.shortcuts import render
from reviseApp.models import Record
from reviseApp import forms
from django.http import HttpResponse
# Create your views here.
def index(request):
    form=forms.NewRecord()
    if request.method=="POST":
        form=forms.NewRecord(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("THANK YOU! GO to /user to views updata record")
        else:
            print("SOMETHING IS ERROR!")


    return render(request,'home.html',{'form':form})
def users(request):
    user_list=Record.objects.order_by('first_name')
    user_dict={'users':user_list}
    return render(request,'users.html',context=user_dict)
