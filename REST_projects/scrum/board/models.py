from django.db import models
from django.utils.translation import ugettext_lazy as _ 
from django.conf import settings
# Create your models here.

class Sprint(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=True, default='')
    description = models.TextField(_("Description"), blank=True, default='')
    end = models.DateField(_("End"), unique=True, auto_now=False, auto_now_add=False)
    

    def __str__(self):
        return self.name or _("Sprint ending %s") % self.end

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

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
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    started = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    due = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    completed = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

