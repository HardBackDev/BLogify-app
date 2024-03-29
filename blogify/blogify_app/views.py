from django.shortcuts import render
from .models import Post

def news_page(request):
    posts = Post.objects.all()
    return render(request, 'news.html', {'posts': posts})

def news_detail_page(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'news_detail.html', {'post': post})

def home_page(request):
    latest_posts = Post.objects.order_by('-created_at')[:4]
    return render(request, 'index.html', {'latest_posts': latest_posts})
    

