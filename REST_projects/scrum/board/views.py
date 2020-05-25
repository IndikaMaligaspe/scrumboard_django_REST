from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sprint , Task, Team
from .serializer import SprintSerializer , TaskSerializer, UserSerializer, TeamSerializer
from django_filters import rest_framework as filters
from .forms import TaskFilter , SprintFilter
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


User = get_user_model()

class DefaultMixins(object):
    authentication_classes = [
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    ]
    
    permission_classes = [permissions.IsAuthenticated,]
    paginate_by =  25
    paginate_by_param = 'page_size'
    max_paginate_by = 100



class SprintViewSet(DefaultMixins, viewsets.ModelViewSet):
    queryset = Sprint.objects.all().order_by('end')
    serializer_class = SprintSerializer
    filter_class = SprintFilter
    search_fields = ('name',)
    ordering_fields = ('end','name',)

    def get_queryset(self):
        qs = super(SprintViewSet, self).get_queryset()
        qs = Sprint.objects.filter(users=self.request.user).order_by('end')        
        return qs

    def perform_create(self, serializer):
        serializer.save()
        return super(SprintViewSet,self).perform_create(serializer)


        
class TeamViewSet(DefaultMixins, viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        qs =  super().get_queryset()
        qs =  Team.objects.filter(users = self.request.user)
        return qs 
    


       
class TaskViewSet(DefaultMixins, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_class = TaskFilter
    # search_fields = ('name', 'description',)
    oredring_fields = ('started','due','order','name',)

class UserViewSet(DefaultMixins, viewsets.ModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD,)
