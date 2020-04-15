from django.shortcuts import render
from bs4 import BeautifulSoup
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from .models import Post
from . import scraper


def home(request):
    stuff_for_frontend ={
        'posts' : Post.objects.all(),
    }
    return render(request, 'scrapping/base.html',stuff_for_frontend)

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

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

def search(request):
    car_list = scraper.scrap()
    print(car_list)
    return render(request, 'scrapping/search.html', {'car_list': car_list})