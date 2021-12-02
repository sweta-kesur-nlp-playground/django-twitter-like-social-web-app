from django.conf import settings
from django.shortcuts import render, redirect
from .models import Comment, Message, BookUser, CustomUser, Profile, Post
from .forms import CommentForm, MessageForm, PostForm, CustomUserCreationForm
from django.template import RequestContext
from django.views import View, generic
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.models import auth
from django.views.generic import ListView, DetailView, UpdateView
from itertools import chain
from django.contrib import messages
from django.urls import reverse_lazy

import facebook

def follow_unfollow_profile(request):
	if request.method == "POST":
		my_profile = Profile.objects.get(user=request.user)
		pk = request.POST.get('profile_pk')
		obj = Profile.objects.get(pk=pk)

		if obj.user in my_profile.following.all():
			my_profile.following.remove(obj.user)
		else:
			my_profile.following.add(obj.user)
		return redirect(request.META.get('HTTP_REFERER'))
	return redirect('profile-list-view')

def posts_of_following_profiles(request):
	# get logged in user profile
	profile = Profile.objects.get(user=request.user)
	# check who we are following
	users = [user for user in profile.following.all()]
	# initial values for variables
	posts = []
	qs = None
	# get the posts of people who we are following
	for u in users:
		p = Profile.objects.get(user=u)
		p_posts = p.post_set.all()
		posts.append(p_posts)
	# our posts
	my_posts = profile.profiles_post()
	posts.append(my_posts)
	# sort and chain querysets and unpack the posts list
	if len(posts)>0:
		qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
	return render(request, 'post.html', {'profile':profile, 'posts':qs})

class CommentView(View):
	form_class = CommentForm
	def post(self, request, *args, **kwargs):
	    if request.is_ajax():
	        form = self.form_class(request.POST)
	        if form.is_valid():
	            form.save()
	            return JsonResponse({"message": "success"})
	        return JsonResponse({"message": "Validation failed"})
	    return JsonResponse({"message": "Wrong request"})
	def get(self,request, *args, **kwargs):
	    return render(request, "blog.html", {})

def register(request):

	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username1 = request.POST['username1']
		password = request.POST['password']
		password2 = request.POST['password2']
		email = request.POST['email']
		gender = request.POST['gender']
		user1 = CustomUser.objects.create_user(
	        first_name = first_name,
	        last_name = last_name,
	        username1 = username1,
	        username = username1,
	        password = password,
	        email = email,
	        gender = gender)
		user1.save()
		return JsonResponse({"message": "success"})

	return render(request, 'register.html', {})

class UserUpdateView(generic.UpdateView):
	# customuser = CustomUser.objects.get(pk=pk)
	form_class = CustomUserCreationForm
	template_name = 'editprofile.html'
	success_url = reverse_lazy('signin')
	# return render(request, 'editprofile.html', {'form':form});

	def get_object(self):
		return self.request.user

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('posts-follow-view')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('signin')

    context = {}
    return render(request, 'register.html', context)

def signout(request):
    auth.logout(request)
    return redirect('home')


class CommentListView(View):
	
	def get(self, request, *args, **kwargs):
		if request.is_ajax():
			comments = Comment.objects.all()
			comment_serializers = serializers.serialize('json', comments)
			return JsonResponse(comment_serializers, safe=False)
		return JsonResponse({"message": "Wrong validation"})

class MessageView(View):
	form_class = MessageForm
	def post(self, request, *args, **kwargs):
	    if request.is_ajax():
	        form = self.form_class(request.POST)
	        if form.is_valid():
	            form.save()
	            return JsonResponse({"message": "success"})
	        return JsonResponse({"message": "Validation failed"})
	    return JsonResponse({"message": "Wrong request"})
	def get(self,request, *args, **kwargs):
	    return render(request, "contact.html", {})

def home(request):
	return render(request, 'index.html', {});

def header(request):
	return render(request, 'header.html', {});

def head(request):
	return render(request, 'head.html', {});

def footer(request):
	return render(request, 'footer.html', {});

def about(request):
	# if request.method == 'POST':
	# 	content = request.POST.get('content')

	# 	if content:
	# 		print('Content:', content)

	# 		fbpost = facebook.GraphAPI(settings.ACCESS_TOKEN)
	# 		fbpost.put_object("me", "feed", message=content)

	# 		return redirect('about')
	
	return render(request, 'about.html', {});

def blog(request):
	return render(request, 'blog.html', {});

# def register(request):
# 	return render(request, 'register.html', {});

def contact(request):
	return render(request, 'contact.html', {});

def handler404(request, exception=None):
    return render(request, '404.html', status=404)

def handler500(request, exception=None):
    return render(request, '500.html', status=500)

class ProfileListView(ListView):
	model = Profile
	template_name = 'main.html'
	context_object_name = 'profiles'	#object_list as default

	def get_queryset(self):
		return Profile.objects.all().exclude(user=self.request.user)

class ProfileDetailView(DetailView):
	model = Profile
	template_name = 'detail.html'

	def get_object(self, **kwargs):
		pk = self.kwargs.get('pk')
		view_profile = Profile.objects.get(pk=pk)
		return view_profile

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		view_profile = self.get_object()
		my_profile = Profile.objects.get(user=self.request.user)
		if view_profile.user in my_profile.following.all():
			follow = True
		else:
			follow = False
		context["follow"] = follow
		return context

def AddPost(request):
	if request.method == 'POST':
		author = Profile.objects.get(user=request.POST['author'])
		body = request.POST['body']
		post = Post(
	        author = author,
	        body = body)
		post.save()
		return JsonResponse({"message": "success"})

	return render(request, 'post.html', {})


