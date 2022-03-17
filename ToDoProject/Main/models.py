from email.policy import default
from random import choices
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Work(models.Model):
    LOW = 0
    NORMAL = 1
    HIGH = 2
    FHIGH = 3
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    date_created = models.DateTimeField(default=timezone.now)
    complete_till = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=(
        (LOW, 'LOW'),
        (NORMAL, 'NORMAL'),
        (HIGH, 'HIGH'),
        (FHIGH, 'FIRST PRIORITY'),
    ), default=2)

    class Meta:
        ordering = ['-priority', '-date_created']

    def __str__(self):
        return self.title

    @property
    def are_you_late(self):
        if self.complete_till < timezone.now():
            return True
        return False