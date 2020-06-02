from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("Hello, Kunja!")
    my_dict={'a':"Django with his Guitar!"}
    return render(request,'app/index.html',context=my_dict)
