from django.conf import settings
from django.shortcuts import render, redirect
from .models import Comment, Message, BookUser, CustomUser
from .forms import CommentForm, MessageForm, RegisterForm, CustomUserCreationForm
from django.template import RequestContext
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import facebook

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

class UserView(View):
	form_class = CustomUserCreationForm
	def post(self, request, *args, **kwargs):
	    if request.is_ajax():
	        form = self.form_class(request.POST)
	        if form.is_valid():
	            form.save()
	            return JsonResponse({"message": "success"})
	        return JsonResponse({"message": "Validation failed"})
	    return JsonResponse({"message": "Wrong request"})
	def get(self,request, *args, **kwargs):
	    return render(request, "register.html", {})

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

# Create your views here.
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

def register(request):
	return render(request, 'register.html', {});

def contact(request):
	return render(request, 'contact.html', {});

def handler404(request, exception=None):
    return render(request, '404.html', status=404)

def handler500(request, exception=None):
    return render(request, '500.html', status=500)
