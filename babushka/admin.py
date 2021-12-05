from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Comment, Message, CustomUser, Post, Profile
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

admin.site.site_header = 'Babushka Dashboard'

class CustomUserAdmin(UserAdmin):
	model = CustomUser
	add_form = CustomUserCreationForm

	fieldsets = (
		*UserAdmin.fieldsets,
		(
			'Additional fields',
			{
				'fields': (
					'gender', 'is_author'
				)
			}
		)
	)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')
	list_filter = ('name',)

class MessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')
	list_filter = ('name',)

class PostAdmin(admin.ModelAdmin):
	list_display = ('author', 'created')
	list_filter = ('author', 'created')

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'created')
	list_filter = ('user', 'created')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)

admin.site.unregister(Group)

