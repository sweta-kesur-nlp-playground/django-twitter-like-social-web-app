from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	customusername = models.CharField(max_length=100)
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
