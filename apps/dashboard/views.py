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
from apps.dashboard.forms import *
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

class NovelGestionView(ListView):
    template_name = "users/novelgestion/list.html"
    model = Novel
    context_object_name = 'novel_list'


class ListChapter(ListView):
    template_name = 'users/novelgestion/view.html'
    model = Chapter 
    context_object_name = 'chapter_list'

    def get_queryset(self):
        user = self.kwargs['pk']
        queryset = Chapter.objects.all()
        queryset = queryset.filter(novel=user)
        return queryset


class CreateRegister(CreateView):
    template_name = "users/usergestion/register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('dashboard:home')


class UpdateRegister(UpdateView):
    template_name = "user/register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('dashboard:home')

def get_status(request,pk):
    fliter = pk
    instance =  Novel.objects.filter(pk=fliter)
    instance.update(status=False)
    return redirect('dashboard:home')


    

