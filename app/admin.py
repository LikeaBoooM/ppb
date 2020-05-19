from django.contrib import admin
from .models import Post, Comment, NewCar, Images, Search

class ImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(NewCar)
admin.site.register(Search)
admin.site.register(Images, ImagesAdmin)