from django.shortcuts import render
from django.http import HttpResponse
from reviseApp import forms
# from reviseApp.models import Topic,Webpage,AccessRecord
# Create your views here.
# def index(request):
#     webpages_list=AccessRecord.objects.order_by('date')
#     date_dict={'access_record':webpages_list}
#     return render(request,'new.html',context=date_dict)
#
# def kunja(request):
#     return HttpResponse("Hello, world!")


def index(request):

    return render(request,'new.html')

def form(request):

    form=forms.Formname()
    if request.method=="POST":
        form=forms.Formname(request.POST)
        if form.is_valid():
            # print("VALIDATION SUCESS!")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    return render(request,'form.html',{'form':form})
