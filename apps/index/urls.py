from django.urls import path
from . import views

app_name = 'index'  
urlpatterns = [

path('', views.IndexView.as_view(), name='home'),
path('register/', views.CreateRegister.as_view(), name='register'),
path('login/', views.LoginView.as_view(), name='login'),

]