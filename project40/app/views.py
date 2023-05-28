from django.shortcuts import render
from app.models import *
from django.views.generic import TemplateView,ListView,DetailView,DeleteView,UpdateView,CreateView
from django.urls import reverse_lazy
# Create your views here.
class homepage(TemplateView):
    template_name='app/home.html'
    

class schoollist(ListView):
    model=School
    context_object_name='schools'    


class schooldetail(DetailView):
    model=School
    context_object_name='schoolobj'

class schoolcreate(CreateView):
    model=School
    fields='__all__'    

class schoolupdate(UpdateView):
    model=School
    fields='__all__'

class schooldelete(DeleteView):
    model=School
    context_object_name='Schoolobject'
    success_url=reverse_lazy('schoollist')
