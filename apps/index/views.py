from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.shortcuts import render
from apps.index.models import *
from apps.index.forms import *
from apps.index.utils import *

class IndexView(TemplateView):
     template_name = "index.html"


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
        context['operation'] = 'Create'
        return context

     def form_valid(self, form):
        form.instance.user_profile = self.request.user
        image_url = self.request.FILES['image']
        print(image_url)
        image_url = upload_image_file(image_url,'userNovel/')
        form.instance.image = image_url
        
            
        return super(CreateUserNovel, self).form_valid(form)


class LoginView(TemplateView):
    template_name = "Login/login.html"
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index:user')
        return super(LoginView, self).get(request, **kwargs)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.login(request)
            login(request, user)
            return redirect('index:user')
        return render(request, self.template_name, {'form': form })

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index:login')
