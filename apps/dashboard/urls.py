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
path('novel_gestion/desactive/<pk>/', views.get_status, name='status'),
path('genre/create/', views.CreateGenre.as_view(), name='genre_create'),
path('genre/list/', views.ListGenre.as_view(), name='list_genre'),
path('genre/update/<pk>', views.UpdateGenre.as_view(), name='update_genre'),
path('sub_genre/create/', views.CreateSubGenre.as_view(), name='sub_genre_create'),
path('sub_genre/update/<pk>/', views.UpdateGenre.as_view(), name='update_sub_genre'),
path('sub_genre/list/', views.ListSubGenre.as_view(), name='list_sub_genre'),
path('new/create/', views.CreateNew.as_view(), name='create_New'),
path('new/list/', views.ListNew.as_view(), name='list_new'),
]