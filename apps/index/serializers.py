from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.index.models import * 


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class RolSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        models = RolUser 
        fields =['url', 'rol_user_name']