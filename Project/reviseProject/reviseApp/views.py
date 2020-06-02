from django.shortcuts import render
from reviseApp import forms
from reviseApp.models import UserModel


from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request,'index.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def special(request):
    return HttpResponse("You are logged in!")
def form(request):

    # registered=False
    if request.method=="POST":
        form=forms.UserForm(data=request.POST)
        url_form=forms.UserURLForm(data=request.POST)

        if form.is_valid() and url_form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)

            profile.user=user



    return render(request,'form.html',{'form':user,'url_form':profile})

def user_login(request):
    if request.method=="POST":

        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')
        user=authenticate(username=user_name,password=pass_word)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTVE")
        else:
            print("Someone tried to login and failed")
            print("Username:{} and password:{}".format(username,password))
            return HttpResponse("Invalid")
    else:

        return render(request,'login.html')
