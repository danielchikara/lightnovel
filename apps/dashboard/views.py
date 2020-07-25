from django.shortcuts import render
from django.views.generic import TemplateView, CreateView,UpdateView,ListView

class DashboardView(TemplateView):
    template_name = "users/index.html"

class UserGestionView(TemplateView):
    template_name = "users/usergestion/list.html"
    model = User
    context_object_name = 'user_list'

