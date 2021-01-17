from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Post

# Create your views here.

def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/index.html', context)

def addPost(request):
    if request.method == "POST":
        #get postdata from request.POST
        title = request.POST['title']
        content = request.POST['post']
        author = request.user
        post = Post.objects.create(title=title, content=content, author=author)
        return redirect('/')
    else:
	# return render of template with form for adding posts (context is empty {})
    
        return render(request, 'blog/add.html', {})

def editPost(request,id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "GET":
        context = {
        "post":post
        }
        return render(request, 'blog/update.html', context)
    else:
        title = request.POST['title']
        post.title = title
        content = request.POST['post']
        post.content = content
        #print('\n\n',request.POST,'\n\n')
        post.save()
        return redirect('/')

def removePost(request,id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def login(request):
    return render(request, 'blog/login.html', {'title': 'Login'})

def register(request):
    return redirect('/')