from django.db import models
from accounts.models import *
from apps.models import *

# Create your models here.

class Group(models.Model):
    members = models.ManyToManyField(Profile)
    title = models.CharField(max_length=200)
    app = models.ForeignKey(applists, on_delete=models.CASCADE)
    description = models.TextField(max_length=800)
    
    def __str__(self):
        return self.title
    