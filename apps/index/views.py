from django.shortcuts import render
from apps.index.models import * 
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView 

# Create your views here.
class IndexView(TemplateView):
     template_name = "index.html"