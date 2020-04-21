from django.contrib import admin
from .models import Post, Comment, NewCar, Images

class ImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(NewCar)
admin.site.register(Images, ImagesAdmin)