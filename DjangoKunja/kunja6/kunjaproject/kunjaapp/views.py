from django.shortcuts import render
from django.http import HttpResponse
from kunjaapp.models import User
# Create your views here.


def index(request):
    return render(request,'app/index.html')



def users(request):
    top=User.objects.order_by('first_name')
    dict={'user':top}
    return render(request,'app/index1.html',context=dict)
