from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class RolUser(models.Model):
    rol_user_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.rol_user_name
    
       
class UserNovel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")    
    rol_user= models.ForeignKey(RolUser, related_name="rol_users", on_delete=models.CASCADE)    
    status = models.BooleanField(default=True)
    email = models.EmailField((), max_length=254)
    date = models.DateField()

    def __str__(self):
        return self.user.username


class Account(models.Model):
    user_novel = models.ForeignKey(UserNovel, related_name="user_novels_accounts", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class ListRead(models.Model):
    account = models.ForeignKey(Account, related_name="accounts_list", on_delete=models.CASCADE)
    name_list =models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.name_list


class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)

    def __str__(self):
        return self.name
    

class SubGenre(models.Model):
    genre = models.ForeignKey(Genre, related_name="genre_subgenre", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)

    def __str__(self):
        return self.name
    

class Novel(models.Model):
    subgenre = models.ForeignKey(SubGenre, related_name="subgenre_novel", on_delete=models.CASCADE)
    account = models.ForeignKey(Account, related_name="accounts_novel", on_delete=models.CASCADE)
    list_read = models.ForeignKey(ListRead, related_name="list_read_novel", on_delete=models.CASCADE)
    name = models.CharField( max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
        

class Chapter(models.Model):
    novel = models.ForeignKey(Novel, related_name="chapter_novel", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

    

    
    
