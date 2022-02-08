import uuid 
from django.utils import timezone
from django.db import models

from django.urls import reverse


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deleted = models.BooleanField(null = True)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    by = models.CharField(max_length=200)
    time = models.TimeField(auto_now=False)
    text = models.CharField(max_length=200, null = True)
    dead = models.BooleanField( null = True)
    parent = models.IntegerField(null = True)
    poll = models.IntegerField(null = True)
    kids = models.IntegerField(null = True)
    url = models.URLField(max_length=200, blank = True, null = True)
    score = models.IntegerField(null = True)
    title = models.CharField(max_length=200)
    parts = models.IntegerField(null = True)
    descendants = models.IntegerField(null = True)


    def __str__(self):
        return self.name



    def get_absolute_url(self): 
        return reverse('news_detail', args=[str(self.id)])


class Type(models.Model):
    name = models.CharField(max_length=20)

