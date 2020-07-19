from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, CreateView,UpdateView,ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.shortcuts import render
from apps.index.models import *
from apps.index.forms import *
from apps.index.utils import *

class IndexView(TemplateView):
    template_name = "index.html"
    
    #def get_context_data(self, **kwargs):
        #context['pk_user'] = self.user.pk


class CreateRegister(CreateView):
    template_name = "user/register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('index:home')


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
        form.instance.user_profile = self.request.user
        image_url = self.request.FILES['image']
        image_url = upload_image_file(image_url,'userNovel/')
        form.instance.image = image_url
        return super(CreateUserNovel, self).form_valid(form)


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
        if self.request.FILES.get('document_file', False):
            image_url = self.request.FILES['image']
            image_url = upload_image_file(image_url,'userNovel/')
            form.instance.image = image_url
        return super(UpdateUserNovel,self).form_valid(form)

class CreateNovel(CreateView):
    template_name = "novels/register.html"
    model = Novel
    form_class = NovelForm
    success_url = reverse_lazy('index:home')

     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'Crear.'
        context['title1'] = 'Creacion de Novela.'
        
        return context

    def form_valid(self, form):
        image_url = self.request.FILES['image']
        image_url = upload_image_file(image_url,'novel/')
        form.instance.image = image_url            
        return super(CreateNovel, self).form_valid(form)


class UpdateNovel(UpdateView):
    template_name = "novels/register.html"
    model = Novel
    form_class = NovelForm
    success_url = reverse_lazy('index:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['image'] = instance.image
        context['operation'] = 'Actualizar'
        context['title1'] = 'Actualizacion de Datos.'
        return context

    def form_valid(self, form):
        if self.request.FILES.get('document_file', False):
            image_url = self.request.FILES['image']
            image_url = upload_image_file(image_url,'userNovel/')
            form.instance.image = image_url
        return super(UpdateUserNovel,self).form_valid(form)


class ListNovel(ListView):
    template_name = 'novels/list.html'
    model = Novel
    context_object_name = 'novel_list'



class CreateChapter(CreateView):
    template_name = "chapters/create.html"
    model = Chapter
    form_class = ChapterForm
    success_url = reverse_lazy('index:home')

     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'Crear.'
        context['title1'] = 'Crear Capitulo'
        return context

    def form_valid(self, form):
        image_url = self.request.FILES['image']
        image_url = upload_image_file(image_url,'Chapter/')
        form.instance.image = image_url            
        return super(CreateNovel, self).form_valid(form)






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
