from django.shortcuts import redirect, render
from django.views import generic 
from .models import Post, Category
from .form import CommentForm

# Create your views here.

def feed(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    if request.user.is_authenticated:
        return render(request, 'blog/member/feed.html', {'posts':posts, 'categories':categories})
    else:
        return render(request, 'blog/anonymous/feed.html', {'posts':posts, 'categories':categories})

def category(request):
    category = Category.objects.all()
    if request.user.is_authenticated:
        return render(request, 'blog/member/category.html', {'category':category})
    else:
        return render(request, 'blog/anonymous/category.html', {'category':category})

def about(request):
    return render(request, 'blog/about.html')

def get_started(request):
    return render(request, 'blog/anonymous/get_started.html')

def category_post(request, slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    if request.user.is_authenticated:
        return render(request, 'blog/member/category_post.html', {'category':category, 'categories':categories})
    else:
        return render(request, 'blog/anonymous/category_post.html', {'category':category, 'categories':categories})

def post_detail(request, category_slug, slug):
    post = Post.objects.get(slug=slug)
    user = request.user
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', category_slug=category_slug, slug=post.slug)

    else:
        form = CommentForm()
    if request.user.is_authenticated:
        return render(request, 'blog/member/post_detail.html', {'post':post, 'form':form})
    else:
        return render(request, 'blog/anonymous/post_detail.html', {'post':post, 'form':form})

