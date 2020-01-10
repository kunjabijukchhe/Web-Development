from django.shortcuts import render
from app.forms import NewUserForm
# Create your views here.
def home(request):
    return render(request,'home.html')
# def other(request):
#     form=NewUserForm()
#     if request.method=='POST':
#         form=NewUserForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return home(request)
#      return render(request,'other.html',{'form':form})
def other(request):
    form=NewUserForm()
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
    return render(request,'other.html',{'form':form})
