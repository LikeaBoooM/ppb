from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Car(models.Model):
    mark = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

