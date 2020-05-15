from django.urls import path
from . import views

app_name = 'index'  
urlpatterns = [

path('', views.IndexView.as_view(), name='home'),
path('register/', views.RegisterView.as_view(), name='register'),

]