from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets
from .models import Sprint , Task
from .serializer import SprintSerializer , TaskSerializer, UserSerializer
from django_filters import rest_framework as filters
from .forms import TaskFilter , SprintFilter

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
    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer
    filter_class = SprintFilter
    search_fields = ('name',)
    ordering_fields = ('end','name',)

class TaskViewSet(DefaultMixins, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_class = TaskFilter
    # search_fields = ('name', 'description',)
    oredring_fields = ('order','name','started','due','completed')

class UserViewSet(DefaultMixins, viewsets.ReadOnlyModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD,)
