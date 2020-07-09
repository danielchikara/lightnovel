from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from apps.index.forms import *
from apps.index.models import *
from django.shortcuts import render

class IndexView(TemplateView):
     template_name = "index.html"


class CreateRegister(CreateView):
     template_name = "user/register.html"
     model = User
     form_class = RegisterForm
     success_url = reverse_lazy('index:home')


class LoginView(TemplateView):
    template_name = "Login/login.html"
    #form_class = LoginForm

    #def get(self, request, *args, **kwargs):
     #   if request.user.is_authenticated:
      #      if request.user.is_staff == True:
       #         return redirect('index:curriculum_vitae_list')
        #    else:
         #       try:
          #          request.user.personal_information.document != None
           #         pk = self.request.user.id
            #        return redirect('index:curriculum_vitae', pk)
             #   except:
              #      return redirect('index:personal')
        #return super(LoginView, self).get(request, **kwargs)

    #def post(self, request):
     #   form = self.form_class(request.POST)
      #  if form.is_valid():
       #     user = form.login(request)
        #    login(request, user)
         #   if request.user.is_staff == True:
          #      return redirect('index:curriculum_vitae_list')
           # else:
            #    try:
             #       request.user.personal_information.document != None
              #      pk = self.request.user.id
               #     return redirect('index:curriculum_vitae', pk)
               # except:
                #    return redirect('index:personal')
       # return render(request, self.template_name, {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index:login')
