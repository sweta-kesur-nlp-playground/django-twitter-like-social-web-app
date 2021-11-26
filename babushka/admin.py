from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Comment, Message, BookUser, CustomUser

admin.site.site_header = 'Babushka Dashboard'

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')
	list_filter = ('name',)

class MessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')
	list_filter = ('name',)

admin.site.register(Comment, CommentAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(BookUser)
admin.site.register(CustomUser)
admin.site.unregister(Group)

