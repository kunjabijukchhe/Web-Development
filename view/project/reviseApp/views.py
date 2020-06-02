from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from reviseApp.models import School
# Create your views here.
# class IndexView(View):
#     def get(self,request):
#         return HttpResponse("Kunja Bijukchhe")
class IndexView(TemplateView):
    template_name='index.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['view']="Kunja Bijukchhe"
        return context

class SchoolListView(ListView):
    model=School

class SchoolDetailView(DetailView):
    model=School
    template_name='reviseApp/school_detail.html'
