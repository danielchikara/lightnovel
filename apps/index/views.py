from django.shortcuts import render
from apps.index.models import * 
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView 
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from apps.index.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
# Create your views here.


#class RolUser(viewsets.ModelViewSet):
 #   queryset = RolUser.objects.all()
  #  serializer_class = RolSerializer
   # permission_classes = [permissions.IsAuthenticated]


class IndexView(TemplateView):
     template_name = "index.html"