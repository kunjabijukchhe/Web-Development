from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from reviseApp.models import School
from django.urls import reverse_lazy
# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'
class SchoolListView(ListView):
    # context_object_name='schools'
    # school_list
    model=School

class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    # school
    model=School
    template_name='reviseApp/school_detail.html'

class SchoolCreateView(CreateView):
    fields=('name','principal','location')
    model=School

class SchoolUpdateView(UpdateView):
    fields=('name','principal','location')
    model=School

class SchoolDeleteView(DeleteView):
    # fields=('name','principal','location')
    success_url= reverse_lazy("reviseApp:list")
    model=School
