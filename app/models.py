from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from PIL import Image


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
    image = models.ImageField(
        upload_to='profile_pics/',
        default='profile_pics/default.jpg')


    def __str__(self):
        return self.mark

    def get_absolute_url(self):
        return reverse('home')

    def upload_image(self, filename):
        return 'post/{}/{}'.format(self.title, filename)

    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
    
        if img.height > 300 or img.width > 300:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.image.path) 

class Images(models.Model):
    post = models.ForeignKey(NewCar, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.post.title + " Image"

class Search(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.CharField(max_length=100)
    model = models.CharField(null=True, max_length=32)
    year_from = models.CharField(default=2010, max_length=32)
    year_to = models.CharField(default=2010, max_length=32)
    petrol = models.CharField(choices=PETROL, max_length=32)
    gear = models.CharField(choices=GEAR, max_length=32)
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.post.author

   

   
