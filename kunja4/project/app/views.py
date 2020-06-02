from django.shortcuts import render
from django.http import HttpResponse
from app.models import Record,Website
# Create your views here.
def index(request):
    #return HttpResponse("Hello, Kunja!")
    web=Website.objects.order_by('name')
    my_dict={'a':web}
    return render(request,'app/index.html',context=my_dict)
