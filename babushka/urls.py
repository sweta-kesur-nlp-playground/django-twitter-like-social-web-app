from django.urls import path, include
from . import views
from .views import CommentView, CommentListView, MessageView

handler404 = 'babushka.views.handler404'
handler500 = 'babushka.views.handler500'

urlpatterns = [
	path('blog/', CommentView.as_view(), name="comment"), 
	path('blog/data', CommentListView.as_view(), name="commentlistview"),
	# path('register/', UserView.as_view(), name="registerview"), 
	path('contact/', MessageView.as_view(), name='message'),
	path('', views.home, name='home'),
	path('home/', views.home, name='home'),
    path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
    path('head/', views.head, name='head'),
	path('contact/', views.contact, name='contact'),
	path('about/', views.about, name='about'),
	path('blog/', views.blog, name='blog'),
	path('register/', views.register, name='register'),
]