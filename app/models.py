from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_with_comment', kwargs={'pk': self.pk})

class Comment(models.Model):
    content = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class NewCar(models.Model):
    DIESEL = 'diesel'
    BENZIN = 'benzin'
    GAS = 'gas'
    AUTOMAT = 'automat'
    MANUAL = 'manual'

    PETROL = [
       (DIESEL, _('Diesel')),
       (BENZIN, _('Benzin')),
       (GAS, _('Gas')),
    ]

    GEAR = [
       (AUTOMAT, _('Automat')),
       (MANUAL, _('Manual')),
    ]

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.CharField(max_length=100)
    model = models.CharField(null=True, max_length=32)
    content = models.TextField()
    year = models.CharField(default=2010, max_length=32)
    price = models.PositiveIntegerField()
    petrol = models.CharField(choices=PETROL, max_length=32)
    gear = models.CharField(choices=GEAR, max_length=32)
     

    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='tire.png', upload_to='profile_pics')


    def __str__(self):
        return self.mark

    def get_absolute_url(self):
        return reverse('home')

    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
    
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) 

class Images(models.Model):
    post = models.ForeignKey(NewCar, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.post.title + " Image"

   

   
