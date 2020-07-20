from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models

# Create your models here.
class SocialUserManager(BaseUserManager):

    def create_user(self, email, password , **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user

class User(AbstractUser):
    username = None
    email = models.EmailField('email address',  unique=True, db_index=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = SocialUserManager()

    def __str__(self):
        return self.email

class RolUser(models.Model):
    rol_user_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.rol_user_name
    
       
class UserNovel(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name="personal_information") 
    username = models.CharField(max_length=150)
    rol_user= models.ForeignKey(RolUser, related_name="rol_users", on_delete=models.CASCADE)    
    status = models.BooleanField(default=True)
    gender = models.CharField(max_length=150)
    image = models.CharField(max_length=500)
    age = models.CharField(max_length=25)

    def __str__(self):
        return self.username



class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    status = models.BooleanField(default=True)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    

class SubGenre(models.Model):
    genre = models.ForeignKey(Genre, related_name="genre_subgenre", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Novel(models.Model):
    subgenre = models.ForeignKey(SubGenre, related_name="subgenre_novel", on_delete=models.CASCADE)
    user_novel = models.ForeignKey(UserNovel,related_name= "user_novels",on_delete=models.CASCADE,default=None, null=True)
    name = models.CharField( max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=True)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name
        

class ReadingList(models.Model):
    user_novel = models.ForeignKey(UserNovel, related_name="accounts_list", on_delete=models.CASCADE)
    list_read = models.ForeignKey(Novel, related_name="list_read_novel", on_delete=models.CASCADE, default=None )
    name_list =models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.name_list


class Chapter(models.Model):
    novel = models.ForeignKey(Novel, related_name="chapter_novel", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    content = models.TextField(max_length=100000)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class News(models.Model): 
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)


    
    
