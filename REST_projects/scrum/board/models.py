from django.db import models
from django.utils.translation import ugettext_lazy as _ 
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Sprint(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, default='')
    description = models.TextField(_("Description"), blank=True, default='')
    end = models.DateField(_("End"), unique=True, auto_now=False, auto_now_add=False)
    users = models.ManyToManyField(User, blank=True)
    

    def __str__(self):
        return self.name or _("Sprint ending %s") % self.end

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

class Team(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=False)
    users = models.ManyToManyField(User, blank=True)
    sprints = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    website = models.CharField(_("website"), max_length=200, blank=True)
    description  = models.CharField(_("Descriptiopn"), max_length=500, blank=True)
  
    class Meta:
       ordering = ['name']
    
    def __str__(self):
        return self.name
  

class Task(models.Model):
    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO, _('Not Started')),
        (STATUS_IN_PROGRESS, _('In Progress')),
        (STATUS_TESTING, _('Testing')),
        (STATUS_DONE, _('Done')),
    )
    
    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField(_("Description"), blank=True, default='')
    sprint = models.ForeignKey(Sprint, blank=True, null=True, on_delete=models.CASCADE)
    order = models.SmallIntegerField(_("Order"), default=0)
    status = models.SmallIntegerField(_("status"), choices=STATUS_CHOICES, default=STATUS_TODO)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    started = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    due = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    completed = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

