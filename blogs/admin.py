from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Event


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'content', 'date_created',)

class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'details', 'date',)


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Event, EventsAdmin)

admin.site.site_header = 'PRIMUS DEI BLOG'
admin.site.site_title = 'Primus Admin Area'
admin.site.index_title = 'Welcome To Primus Admin Area'
