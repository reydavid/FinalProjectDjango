from django.urls import path, include
from . import views

#app_name="blog" breaks the views for anything with <id>

urlpatterns = [
  path('', views.index),
  path('about/', views.about, name='about'),
  path('addpost/', views.addPost, name='addpost'),
  path('editpost/<id>/', views.editPost, name='editpost'),
  path('removepost/<id>/', views.removePost, name='removepost'),
  path('login', views.login, name='login'),
  path('register', views.register, name='register')
]