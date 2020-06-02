from django.shortcuts import render
from app.forms import UserForm,UserProfileInfoForm
#
# # Create your views here.
# def index(request):
#     context_dict={'text':'hello world','number':100}
#     return render(request,'app/index.html',context_dict)
#
# def other(request):
#     return render(request,'app/other.html')
#
# def main(request):
#     return render(request,'app/main.html')
def index(request):

    return render(request,'app1/index.html')
def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.Post)
        profile_form=UserProfileInfoForm(data=request.Post)
        if user_form.is_valid and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request>FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'app1/registation.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
