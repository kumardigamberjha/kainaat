from django.contrib import admin

from Blog.models import Blog, Playlist, Comment

admin.site.register(Blog)
admin.site.register(Playlist)
admin.site.register(Comment)


# admin.site.register(BlogsTags)
