from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def index(request):
    # return HttpResponse("KUNJA BIJUKCHHE")
def index(requestByKunja):#use for template
    my_dict={'a':'hello kunja!'}
    #return render(requestByKunja,'index.html',context=my_dict)
    return render(requestByKunja,'kunjapp/index1.html',context=my_dict)
