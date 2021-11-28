from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	username1 = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	gender = models.CharField(max_length=100)
	is_author = models.BooleanField(default=True)
	is_reader = models.BooleanField(default=False)
	
class Comment(models.Model):

	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	comment = models.TextField()

class Message(models.Model):

	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	message = models.TextField()

class BookUser(models.Model):

	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	gender = models.CharField(max_length=100)

class Profile(models.Model):
	user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
	following = models.ManyToManyField(CustomUser, related_name='following', blank=True)
	bio = models.TextField(default='No bio...')
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def profiles_post(self):
		return self.post_set.all()

	def __str__(self):
		return str(self.user.username)

	class Meta:
		ordering = ('-created',)

class Post(models.Model):
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	body = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.body)[:30]

	class Meta:
		ordering = ('-created',)

