from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
	gender = models.CharField(max_length=100)
	is_author = models.BooleanField(default=False)
	
class Comment(models.Model):

	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	comment = models.TextField()

class Message(models.Model):

	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	message = models.TextField()

class Profile(models.Model):
	user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
	following = models.ManyToManyField(CustomUser, related_name='following', blank=True)
	bio = models.TextField(default='No bio...')
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def profiles_post(self):
		return self.post_set.all()

	def __str__(self):
		return str(self.user)

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

