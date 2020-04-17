from django.shortcuts import render
from bs4 import BeautifulSoup
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import requests
from django.shortcuts import get_object_or_404 , HttpResponseRedirect
from .models import Post, Comment
from . forms import CommentForm 
from . import scraper


def home(request):
    stuff_for_frontend ={
        'posts' : Post.objects.all(),
    }
    return render(request, 'scrapping/base.html',stuff_for_frontend)

def post_detail_with_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-id')

    if request.method == "POST":
        commentForm = CommentForm(request.POST or none)
        if commentForm.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post = post, author = request.user, content = content)
            comment.save()

            return HttpResponseRedirect(post.get_absolute_url())
    else :
        commentForm = CommentForm()

    
    stuff_for_frontend ={
        'object' : post,
        'comments' : comments,
        'commentForm' : commentForm,
    }

    return render(request, 'app/post_detail.html', stuff_for_frontend)


class PostListView(ListView):
    model = Post
    template_name = 'scrapping/base.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def search(request):
    car_list = scraper.scrap()
    print(car_list)
    return render(request, 'scrapping/search.html', {'car_list': car_list})