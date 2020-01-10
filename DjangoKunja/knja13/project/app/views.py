from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'main.html')


def html(request):
    my_dict={'a':'Kunja Bijukchhe'}
    return render(request,'one.html',context=my_dict)
def html1(request):
    my_dict={'a':100}
    return render(request,'two.html',context=my_dict)
