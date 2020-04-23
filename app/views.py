from django.shortcuts import render
from bs4 import BeautifulSoup
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import requests
from django.shortcuts import get_object_or_404 , HttpResponseRedirect, redirect
from .models import Post, Comment, Images, NewCar
from . forms import CommentForm, NewCarForm, SearchForm
from . import scraper
from django.forms import modelformset_factory


def home(request):
    stuff_for_frontend ={
        'posts' : Post.objects.all(),
        'cars' : NewCar.objects.all(),
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

def newCarTwo(request):
    ImageFormset =  modelformset_factory(Images, fields=('image',), extra=4)
    if request.method == 'POST':
        form = NewCarForm(request.POST or None, request.FILES or None)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            for f in formset:
                try:
                    photo = Images(post=post, image=f.cleaned_data['image'])
                    photo.save()
                    
                except Exception as e:
                    break
            return redirect('home')
    else :
        form = NewCarForm()
        formset = ImageFormset(queryset=Images.objects.none())
        
    
    stuff_for_frontend = {
        'form' : form,
        'formset' : formset,
    }

    return render(request, 'app/newcar_form.html', stuff_for_frontend)


class PostListView(ListView):
    model = Post
    template_name = 'scrapping/base.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class CarCreateView(LoginRequiredMixin, CreateView):
    model = NewCar
    fields = ('mark', 'image', 'content',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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
    form = SearchForm(request.POST)
    if form.is_valid():
        mark = form.cleaned_data['mark']
        model = form.cleaned_data['model']
        year_from = form.cleaned_data['year_from']
        year_to = form.cleaned_data['year_to']
        petrol = form.cleaned_data['petrol']
        gear = form.cleaned_data['gear']

        car_list = scraper.scrap()

    car_list = scraper.scrap()
    print(car_list)
    return render(request, 'scrapping/search.html', {'car_list': car_list, 'form': form,})