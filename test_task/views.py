from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'test_task/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'test_task/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'test_task/about.html', {'title': 'About title'})

