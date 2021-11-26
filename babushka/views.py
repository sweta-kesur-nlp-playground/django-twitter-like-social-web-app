from django.conf import settings
from django.shortcuts import render, redirect
from .models import Comment, Message, BookUser, CustomUser
from .forms import CommentForm, MessageForm, RegisterForm, CustomUserCreationForm
from django.template import RequestContext
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.models import auth
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

def register(request):

    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username1 = request.POST['username1']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        gender = request.POST['gender']

        if password == password2: 
            
            if CustomUser.objects.filter(username1=username1).exists():
                messages.info(request, 'username taken')
                return redirect('register')

            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')

            else:
                user = CustomUser.objects.create_user(username1=username1, password=password, email=email, first_name=first_name, last_name=last_name, gender=gender)
                user.save()
                print(request, 'user created')

        else:
            messages.info(request, 'Password not matching...')
            return redirect('register')

        return redirect('home')

    else:
        return render(request, 'register.html', {})

# class UserView(View):
# 	form_class = CustomUserCreationForm
# 	def post(self, request, *args, **kwargs):
# 	    if request.is_ajax():
# 	        form = self.form_class(request.POST)
# 	        if form.is_valid():
# 	            form.save()
# 	            return JsonResponse({"message": "success"})
# 	        return JsonResponse({"message": "Validation failed"})
# 	    return JsonResponse({"message": "Wrong request"})
# 	def get(self,request, *args, **kwargs):
# 	    return render(request, "register.html", {})

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
