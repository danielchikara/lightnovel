from apps.index.models import *
from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("__all__")
