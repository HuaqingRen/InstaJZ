from django.contrib import admin

from Insta.models import Post,Post2, InstaUser, Like, UserConnection

# Register your models here.
admin.site.register(Post)
admin.site.register(Post2)
admin.site.register(InstaUser)
admin.site.register(Like)
admin.site.register(UserConnection)