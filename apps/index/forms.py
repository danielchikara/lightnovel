
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from apps.index.models import *
from django import forms
#register,login logout


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


class UserNovelForm(forms.ModelForm):
    class Meta:
        model = UserNovel
        exclude = ('user_profile','image','status',)


class NovelForm(forms.ModelForm):
    class Meta:
        model = Novel
        exclude = ('image','status','user_novel',)


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        exclude = ('novel','image',)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Este usuario y contraseña no coinciden, intenta de nuevo.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user