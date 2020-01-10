from django.shortcuts import render
from django.http import HttpResponse
from app.models import Topic,Webpage,AccessRecord
from app.models1 import User
# Create your views here.

def index(request):
    # my_dic={'insert_me':'hello i am from views.py'}
    # return render(request,'index.html',context=my_dic)
    # my_dic={'insert_me':'hello i am coming from app/index.html'}
    # return render(request,'app/index.html',context=my_dic)


    # webpages_list=AccessRecord.objects.order_by('date')
    # date_dict={'access_records':webpages_list}
    # return render(request,'app/index.html',context=date_dict)
    top=Webpage.objects.order_by('name')
    date_dict={'access_records':top}
    return render(request,'app/index1.html',context=date_dict)



def user(request):
    user_list=User.objects.order_by('first_name')
    user_dict={'users':user_list}
    return render(request,'app/index2.html',context=user_dict)
