from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Comment, Message, BookUser, CustomUser, Post, Profile
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

admin.site.site_header = 'Babushka Dashboard'

class CustomUserAdmin(UserAdmin):
	model = CustomUser
	add_form = CustomUserCreationForm

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')
	list_filter = ('name',)

class MessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')
	list_filter = ('name',)

admin.site.register(Comment, CommentAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)
admin.site.register(Profile)

admin.site.unregister(Group)

