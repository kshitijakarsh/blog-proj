from django.shortcuts import render
from .models import Posts

# Create your views here.

def home(request):
    context = {
        'posts' : Posts.objects.all()
    }
    return render(request, 'blog/homepage.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def post(request):
    return render(request, 'blog/blogpost.html', {'title': 'title'})

def newpost(request):
    return render(request, 'blog/newpost.html', {'title': 'New Post'})

