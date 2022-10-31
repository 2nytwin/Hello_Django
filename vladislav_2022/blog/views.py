from django.shortcuts import render
from .models import Comment, Post


def blog_index(request):
    posts = Post.objects.all().orderby('created_on')[:-1]
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog_detail.html', context)