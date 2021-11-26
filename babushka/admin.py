from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Comment, Message, BookUser, CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

admin.site.site_header = 'Babushka Dashboard'

class CustomUserAdmin(UserAdmin):
	model = CustomUser
	add_form = CustomUserCreationForm

	fieldsets = (
		*UserAdmin.fieldsets,
		(
			'User role',
			{
				'fields': (
					'is_author',
					'is_reader',
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

admin.site.register(Comment, CommentAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(BookUser)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
