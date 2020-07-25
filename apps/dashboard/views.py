from django.shortcuts import render
from django.views.generic import TemplateView, CreateView,UpdateView,ListView

class DashboardView(TemplateView):
    template_name = "users/index.html"

class UserGestionView(TemplateView):
    template_name = "user/usergestion/list.html"

