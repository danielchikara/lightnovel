from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.index.forms import *
from apps.index.models import *
from django.shortcuts import render

class IndexView(TemplateView):
     template_name = "index.html"

class RegisterView(TemplateView):
     template_name = "user/register.html"

class CreateRegister(CreateView):
     template_name = "user/register.html"
     model = User