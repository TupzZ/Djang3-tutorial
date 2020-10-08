from django.shortcuts import render, get_object_or_404
from .models import Blog

def allBlogs(request):
    blogsCount = Blog.objects.all().count()
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/allBlogs.html', {'blogs': blogs, 'blogsCount': blogsCount})

def detail(request, blogId):
    blog = get_object_or_404(Blog, pk=blogId)
    return render(request, 'blog/detail.html', {'blog': blog})
