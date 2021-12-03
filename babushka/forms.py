from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Message, CustomUser, Post

class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model = CustomUser
		# fields = "__all__"
		fields = ["first_name", "last_name", "email", "gender", "is_author"]

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ["name", "email", "comment"]

class MessageForm(forms.ModelForm):

	class Meta:
		model = Message
		fields = ["name", "email", "message"]

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ["author", "body"]

