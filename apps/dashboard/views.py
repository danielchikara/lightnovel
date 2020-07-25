from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic import TemplateView, CreateView,UpdateView,ListView
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.core.files.base import ContentFile
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.shortcuts import render
from apps.index.models import *
from apps.index.forms import *
from apps.index.utils import *
from skimage.io import imread
import numpy
import cv2

class DashboardView(TemplateView):
    template_name = "users/index.html"

class UserGestionView(ListView):
    template_name = "users/usergestion/list.html"
    model = User
    context_object_name = 'user_list'

class CreateRegister(CreateView):
    template_name = "user/register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('dashboard:home')


class UpdateRegister(UpdateView):
    template_name = "user/register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('dashboard:home')
    

