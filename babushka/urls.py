from django.urls import path, include
from . import views
from .views import CommentView, CommentListView, MessageView, ProfileListView, ProfileDetailView, follow_unfollow_profile, posts_of_following_profiles

handler404 = 'babushka.views.handler404'
handler500 = 'babushka.views.handler500'

urlpatterns = [
	path('blog/', CommentView.as_view(), name="comment"), 
	path('addpost/', views.AddPost, name="addpost"), 
	path('blog/data', CommentListView.as_view(), name="commentlistview"),
	path('switch_follow/', follow_unfollow_profile, name="follow-unfollow-view"),
	path('profiles/', ProfileListView.as_view(), name="profile-list-view"), 
	path('profile/<pk>/', ProfileDetailView.as_view(), name="profile-detail-view"), 
	path('home/', views.posts_of_following_profiles, name='posts-follow-view'),
	path('contact/', MessageView.as_view(), name='message'),
	path('', views.home, name='home'),
    path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
    path('head/', views.head, name='head'),
	path('contact/', views.contact, name='contact'),
	path('about/', views.about, name='about'),
	path('blog/', views.blog, name='blog'),
	path('register/', views.register, name='register'),
	path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]