from django.contrib import admin
from .models import Sprint, Task, Team


# Register your models here.

@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
