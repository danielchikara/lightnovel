from django.urls import path
from . import views

app_name = 'dashboard'  
urlpatterns = [

path('', views.DashboardView.as_view(), name='home'),
path('usergestion/', views.UserGestionView.as_view(), name='usergestion'),

]