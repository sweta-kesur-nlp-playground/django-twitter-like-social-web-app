from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Message, BookUser, CustomUser

class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model = CustomUser
		# fields = "__all__"
		fields = ["username", "first_name", "last_name", "email", "password", "gender", "is_author", "is_reader"]

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ["name", "email", "comment"]

class MessageForm(forms.ModelForm):

	class Meta:
		model = Message
		fields = ["name", "email", "message"]

class RegisterForm(forms.ModelForm):

	class Meta:
		model = BookUser
		fields = ["username", "firstname", "lastname", "email", "password", "gender"]