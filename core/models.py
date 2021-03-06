from turtle import title
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Settings(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    hcode = models.TextField(null=True,blank=True)
    fcode = models.TextField(null=True,blank=True)
    styles = models.TextField(null=True,blank=True)
    