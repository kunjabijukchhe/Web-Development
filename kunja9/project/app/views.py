from django.shortcuts import render
from app.forms import NewUserForm
# Create your views here.
def index(request):
    return render(request,'home.html')

def end(request):
    return render(request,'end.html')


def users(request):
    form=NewUserForm()
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            print("Password:"+form.cleaned_data['password'])

            form.save(commit=True)
            return end(request)
    return render(request,'form.html',{'form':form})
