from django.urls import path
from . import views

app_name = 'index'  
urlpatterns = [

path('', views.IndexView.as_view(), name='home'),
path('register/', views.CreateRegister.as_view(), name='register'),
path('login/', views.LoginView.as_view(), name='login'),
path('logout/', views.logout_view, name='logout'),
path('chapter/', views.ChapterView.as_view(), name='chapter'),
path('index/user_novel/create/', views.CreateUserNovel.as_view(), name='user'),
path('index/user_novel/update/<pk>/', views.UpdateUserNovel.as_view(), name='userupdate'),
path('index/novel/create/', views.CreateNovel.as_view(), name='novel_create'),
path('index/novel/update/<pk>/', views.UpdateNovel.as_view(), name='novel_update'),
path('index/novel/list/', views.ListNovel.as_view(), name='novel_list'),
path('index/chapter/create/<pk>/', views.CreateChapter.as_view(), name='chapter_create'),
path('index/chapter/update/<pk>/', views.UpdateChapter.as_view(), name='chapter_update'),
path('index/chapter/list/<pk>/', views.ListChapter.as_view(), name='chapter_list'),
path('index/news/list/', views.NewList.as_view(), name='news_list'),


]