from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from apps.index.models import *
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('rol_user','email','password1','password2',)

    def save(self, commit=True):   
        instance= super(UserCreationForm, self).save(commit=False) # Call the real save() method
        password1 = self.cleaned_data['password1']

        if commit:
            instance.set_password(password1)
            instance.save() 
        #   User.objects.create(user=instance  ) 
        return instance


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        exclude = ('image',)

class SubGenreForm(forms.ModelForm):
    class Meta: 
        model = SubGenre
        exclude = ('image',)

class NewsForm(forms.ModelForm):
    class Meta:
        model = News 
        exclude = ('image',)
