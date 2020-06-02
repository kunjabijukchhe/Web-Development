from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from reviseApp.models import School
from django.urls import reverse_lazy
# Create your views here.
class Index(TemplateView):
    template_name='index.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['view']="KUNJA BIJUKCHHE"
        return context
class SchoolViewList(ListView):
    model=School

class SchoolDetailList(DetailView):
    model=School
    template_name='reviseApp/school_detail.html'
class SchoolCreateView(CreateView):
    model=School
    fields=('name','principal','location')

class SchoolUpdateView(UpdateView):
    model=School
    fields='__all__'
class SchoolDeteteView(DeleteView):
    success_url=reverse_lazy("reviseApp:list")
    model=School
