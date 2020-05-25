import django_filters
from django_filters import rest_framework as filters
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

from .models import Task, Sprint

User = get_user_model()

class NullFilter(django_filters.BooleanFilter):
    def filter(self, qs, value):
        if value is not None:
            return qs.filter(**{'%__isnull' % self.name: value})
        return qs


class SprintFilter(filters.FilterSet):
    
    end = filters.DateFilter(lookup_expr='gte')
    # user = filters.ModelMultipleChoiceFilter(field_name='users',queryset=Sprint.objects.filter(users__icontains=User.USERNAME_FIELD))
    # end_max = filters.DateFilter(lookup_expr='lte')
    
    class Meta:
        model = Sprint
        fields = ('end','users',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['users'].extra.update({'to_field_name':User.USERNAME_FIELD})


class TaskFilter(filters.FilterSet):
    class Meta:
        model = Task
        fields = ('sprint','assigned')

    def __init__(self, *args, ** kwargs):
        super().__init__(*args, **kwargs)
        self.filters['assigned'].extra.update({'to_field_name': User.USERNAME_FIELD})