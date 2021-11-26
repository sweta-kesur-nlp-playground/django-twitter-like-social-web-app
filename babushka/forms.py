from django import forms
from .models import Comment, Message, BookUser, CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model = CustomUser
		fields = "__all__"

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