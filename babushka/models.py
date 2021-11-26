from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
	is_author = models.BooleanField(default=True)
	is_reader = models.BooleanField(default=False)
	gender = models.CharField(max_length=100)
	
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
