from django.shortcuts import render
from app.forms import NewUser,NewFirstUser
# Create your views here.
def index(request):
    form=NewUser()
    if request.method=="POST":
        form=NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return new(request)
    return render(request,'two.html',{'form':form})

def users(request):
    form=NewFirstUser()
    if request.method=='POST':
        form=NewFirstUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # return index(request)
    return render(request,'onr.html',{'form':form})

def new(request):
    return render(request,'three.html')
