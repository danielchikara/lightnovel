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


def resized_image(path, folder):   
    image = imread(path,plugin='matplotlib')
    width = 250
    height = 334
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    color_correct = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    success, buffer = cv2.imencode(".jpg", color_correct)
    new_image = ContentFile(buffer)
    new_image.content_type = 'image/jpeg'
    image_url = upload_image_file(new_image, folder)
    return image_url
        

class IndexView(ListView):
    template_name = "index.html"
    model = Novel
    context_object_name = 'novel_list'
    
    

class ChapterView(TemplateView):
    template_name = "chapters/view.html"


class CreateRegister(CreateView):
    template_name = "user/register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('index:home')

@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateUserNovel(CreateView):
    template_name = "user/user.html"
    model = UserNovel
    form_class = UserNovelForm
    success_url = reverse_lazy('index:home')
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title1'] = 'Registro  de Datos. '
        context['operation'] = 'Registrar'
        return context

    def form_valid(self, form):
        print(self.request.user)
        form.instance.user_profile = self.request.user
        image_url = self.request.FILES['image']
        image_url = upload_image_file(image_url,'userNovel/')
        form.instance.image = image_url
        return super(CreateUserNovel, self).form_valid(form)


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateUserNovel(UpdateView):
    template_name = "user/user.html"
    model = UserNovel
    form_class = UserNovelForm
    success_url = reverse_lazy('index:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['image'] = instance.image
        context['operation'] = 'Actualizar'
        context['title1'] = 'Actualizacion de Datos.'
        return context

    def form_valid(self, form):
        form.instance.user_profile = self.request.user
        if self.request.FILES.get('image', False):
            image_url = self.request.FILES['image']
            image_url = upload_image_file(image_url,'userNovel/')
            form.instance.image = image_url
        return super(UpdateUserNovel,self).form_valid(form)

@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateNovel(CreateView):
    template_name = "novels/register.html"
    model = Novel
    form_class = NovelForm
    
    def get_queryset(self):
        user = self.request.user.id
        queryset = Novel.objects.all()
        queryset = queryset.filter(user_novel__user_profile=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'Crear.'
        context['title1'] = 'Creacion de Novela.'
        return context

    def form_valid(self, form):
        form.instance.user_novel = self.request.user.personal_information
        image_url = self.request.FILES['image']
        image_url = resized_image(image_url,'novel/')
        form.instance.image = image_url            
        return super(CreateNovel, self).form_valid(form)

    def get_success_url(self):
        pk = self.object.pk
        return reverse('index:chapter_create', kwargs={'pk': pk})


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateNovel(UpdateView):
    template_name = "novels/register.html"
    model = Novel
    form_class = NovelForm
    success_url = reverse_lazy('index:home')

    def get_queryset(self):
        user = self.request.user.id
        queryset = Novel.objects.all()
        queryset = queryset.filter(user_novel__user_profile=user)
        return queryset
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['image'] = instance.image
        context['operation'] = 'Actualizar'
        context['title1'] = 'Actualizacion de Datos.'
        return context

    def form_valid(self, form):
        form.instance.user_novel = self.request.user.personal_information
        if self.request.FILES.get('image', False):
            image_url = self.request.FILES['image']
            image_url = resized_image(image_url,'novel/')
            form.instance.image = image_url
        return super(UpdateNovel,self).form_valid(form)


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListNovel(ListView):
    template_name = 'novels/list.html'
    model = Novel
    context_object_name = 'novel_list'

    def get_queryset(self):
        user = self.request.user.id
        print(user)
        queryset = Novel.objects.all()
        queryset = queryset.filter(user_novel__user_profile=user)
        print(queryset)
        return queryset

    
@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class CreateChapter(CreateView):
    template_name = "chapters/register.html"
    model = Chapter
    form_class = ChapterForm
    success_url = reverse_lazy('index:home')

    def get_queryset(self):
        user = self.request.user.id
        queryset = Chapter.objects.all()
        queryset = queryset.filter(novel__user_novel__user_profile=user)
        return queryset
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'Crear.'
        context['title1'] = 'Crear Capitulo'
        return context

    def form_valid(self, form):
        pk_ = get_object_or_404(Novel, pk=self.kwargs['pk'])
        form.instance.novel = pk_
        image_url = self.request.FILES['image']
        image_url = upload_image_file(image_url,'Chapter/')
        form.instance.image = image_url            
        return super(CreateChapter, self).form_valid(form)


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class UpdateChapter(UpdateView):
    template_name = "chapters/register.html"
    model = Chapter
    form_class = ChapterForm
    success_url = reverse_lazy('index:home')
    
    def get_queryset(self):
        user = self.request.user.id
        queryset = Chapter.objects.all()
        queryset = queryset.filter(novel__user_novel__user_profile=user)
        return queryset
    
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
            image_url = upload_image_file(image_url,'Chapter/')
            form.instance.image = image_url
        return super(UpdateChapter,self).form_valid(form)


@method_decorator(login_required(login_url=reverse_lazy('index:login')), name='dispatch')
class ListChapter(ListView):
    template_name = 'chapters/list.html'
    model = Chapter 
    context_object_name = 'chapter_list'

    def get_queryset(self):
        user = self.request.user.id
        queryset = Chapter.objects.all()
        queryset = queryset.filter(novel__user_novel__user_profile=user)
        return queryset

    

class LoginView(TemplateView):
    template_name = "Login/login.html"
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                request.user.personal_information != None
                pk = self.request.user.personal_information.id
                return redirect('index:userupdate',pk)
            except:
                return redirect('index:user')
        return super(LoginView, self).get(request, **kwargs)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.login(request)
            login(request, user)
            try: 
                request.user.personal_information != None
                
                return redirect('index:home')
            except:
                return redirect('index:user')
        return render(request, self.template_name, {'form': form })


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index:login')
