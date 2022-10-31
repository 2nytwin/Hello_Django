from django.shortcuts import render
from .models import Comment


def blog_index(request):
    comms = Comment.objects.all()
    context = {
        'comments': comms
    }
    return render(request, context)


def blog_detail(request, pk):
    comm = Comment.objects.get(pk=pk)
    context = {
        'comment': comm
    }
    return render(request, context)