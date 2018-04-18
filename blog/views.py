from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment


def allblogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/allblogs.html', {'allblogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog=blog_id)

    context = {
        'blog': blog,
        'comments': comments,
    }

    return render(request, 'blog/detail.html', context)
