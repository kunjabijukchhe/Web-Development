from django.shortcuts import render
from app.forms import newUser, newUserPass
from app.models import User
# Create your views here.
#
# def index(request):
#     return HttpResponse("hello world!")
def index(request):
    form=newUser()
    if request.method=="POST":
        form=newUser(request.POST)
        if form.is_valid():
            form.save(commit=True)

    return render(request,'one.html',{'form':form})


def users(request):
    form=newUserPass()
    if request.method=="POST":
        form=newUserPass(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'two.html',{'form':form})

def thank(request):
    user_list=User.objects.order_by('First_name')
    user_dict={'users':user_list}
    return render(request,'thankyou.html',context=user_dict)
