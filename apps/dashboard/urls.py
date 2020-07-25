from django.urls import path
from . import views

app_name = 'dashboard'  
urlpatterns = [

path('', views.DashboardView.as_view(), name='home'),
path('user_gestion/', views.UserGestionView.as_view(), name='user_gestion'),
path('user_gestion/create/', views.CreateRegister.as_view(), name='create_register'),
path('user_gestion/update<pk>/', views.UpdateRegister.as_view(), name='update_register'),
path('novel_gestion/', views.NovelGestionView.as_view(), name='novel_gestion'),
path('novel_gestion/chapter_list/<pk>/', views.ListChapter.as_view(), name='novel_chapter'),
]