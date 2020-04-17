from django.contrib import admin
from .models import Post, Comment, NewCar

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(NewCar)