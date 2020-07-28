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

@method_decorator(user_passes_test(lambda u: u.rol_user.rol_user_name == "Administrador" or u.rol_user.rol_user_name == "Administrador Secundario", login_url=reverse_lazy('index:login')), name='dispatch')
class DashboardView(TemplateView):
    template_name = "users/index.html"
@method_decorator(user_passes_test(lambda u: u.rol_user.rol_user_name == "Administrador", login_url=reverse_lazy('index:login')), name='dispatch')
class UserGestionView(ListView):
    template_name = "users/usergestion/list.html"
    model = User
    context_object_name = 'user_list'


@method_decorator(user_passes_test(lambda u: u.rol_user.rol_user_name == "Administrador" or u.rol_user.rol_user_name == "Administrador Secundario", login_url=reverse_lazy('index:login')), name='dispatch')
class NovelGestionView(ListView):
    template_name = "users/novelgestion/list.html"
    model = Novel
    context_object_name = 'novel_list'

@method_decorator(user_passes_test(lambda u: u.rol_user.rol_user_name == "Administrador" or u.rol_user.rol_user_name == "Administrador Secundario", login_url=reverse_lazy('index:login')), name='dispatch')
class ListChapter(ListView):
    template_name = 'users/novelgestion/view.html'
    model = Chapter 
    context_object_name = 'chapter_list'

    def get_queryset(self):
        user = self.kwargs['pk']
        queryset = Chapter.objects.all()
        queryset = queryset.filter(novel=user)
        return queryset

@method_decorator(user_passes_test(lambda u: u.rol_user.rol_user_name == "Administrador" , login_url=reverse_lazy('index:login')), name='dispatch')
class CreateRegister(CreateView):
    template_name = "users/usergestion/register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('dashboard:user_gestion')


@method_decorator(user_passes_test(lambda u: u.rol_user.rol_user_name == "Administrador", login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateRegister(UpdateView):
    template_name = "users/usergestion/register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('dashboard:home')

def get_status(request,pk):
    fliter = pk
    instance =  Novel.objects.filter(pk=fliter)
    instance.update(status=False)
    return redirect('dashboard:home')

@method_decorator(user_passes_test(lambda u: u.rol_user.rol_user_name == "Administrador", login_url=reverse_lazy('index:login')), name='dispatch')
class CreateGenre(CreateView):
    template_name = "users/genregestion/register.html"
    model = Genre
    form_class = GenreForm
    success_url = reverse_lazy('dashboard:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'Crear'
        context['title1'] = 'Crear  Usuarios.'
        return context
    
    def form_valid(self, form):
        image_url = self.request.FILES['image']
        image_url = upload_image_file(image_url,'Genre/')
        form.instance.image = image_url            
        return super(CreateGenre, self).form_valid(form)

@method_decorator(user_passes_test(lambda u: u.rol_user.rol_user_name == "Administrador", login_url=reverse_lazy('index:login')), name='dispatch')
class ListGenre(ListView):
    template_name = "users/genregestion/list.html"
    model = Genre
    context_object_name = 'genre_list'

    
@method_decorator(user_passes_test(lambda u: u.rol_user.rol_user_name == "Administrador", login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateGenre(UpdateView):
    template_name = "users/genregestion/register.html"
    model = Genre
    form_class = GenreForm
    success_url = reverse_lazy('dashboard:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['image'] = instance.image
        context['operation'] = 'Actualizar'
        context['title1'] = 'Actualizacion de Datos.'
        return context

    def form_valid(self, form):
        if self.request.FILES.get('image', False):
            image_url = self.request.FILES['image']
            image_url = upload_image_file(image_url,'Genre/')
            form.instance.image = image_url            
        return super(CreateGenre, self).form_valid(form)



class CreateSubGenre(CreateView):
    template_name = "users/subgengestion/register.html"
    model = SubGenre
    form_class = SubGenreForm
    success_url = reverse_lazy('dashboard:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'Crear'
        context['title1'] = 'Crear  subgenero.'
        return context


class UpdateGenre(UpdateView):
    template_name = "users/subgengestion/register.html"
    model = SubGenre
    form_class = SubGenreForm
    success_url = reverse_lazy('dashboard:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'Actualizar'
        context['title1'] = 'Actualizar  subgenero.'
        return context

class ListSubGenre(ListView):
    template_name = "users/subgengestion/list.html"
    model = SubGenre
    context_object_name = 'subgen_list'

class CreateNew(CreateView):
    template_name = "users/newgestion/register.html"
    model = News
    form_class = NewsForm
    success_url = reverse_lazy('dashboard:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'Guardar Noticia'
        context['title1'] = 'Crear  Noticia.'
        return context

    def form_valid(self, form):
        image_url = self.request.FILES['image']
        image_url = upload_image_file(image_url,'News/')
        form.instance.image = image_url            
        return super(CreateNew, self).form_valid(form)

class ListNew(ListView):
    template_name = "users/newgestion/list.html"
    model = News
    context_object_name = 'new_list'
    