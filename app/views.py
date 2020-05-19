from django.shortcuts import render
from bs4 import BeautifulSoup
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import requests
from django.shortcuts import get_object_or_404 , HttpResponseRedirect, redirect
from . models import Post, Comment, Images, NewCar
from . forms import CommentForm, NewCarForm, SearchForm, NewPostForm
from . import scraper
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required

def newPost(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save()
    else :
        form = NewPostForm()

    stuff_for_frontend = {
        'form' : form,
    }

    return render(request, 'app/post_form.html', stuff_for_frontend)


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

@login_required
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
    template_name = 'app/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5 

class CarListView(ListView):
    model = NewCar
    template_name = 'app/cars.html'
    context_object_name = 'cars'
    

class PostDetailView(DetailView):
    model = Post

class CarCreateView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = NewCar
    fields = ('mark', 'image', 'content',)


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content',]
    template_name = 'app/post_form.html'
   # success_url = reverse_lazy('home')
    
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

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '../../../posts'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def search(request):
    car_list = []
    form = SearchForm(request.POST or None)
    dane = []

    if form.is_valid():
        mark = form.cleaned_data['mark']
        model = form.cleaned_data['model']
        year_from = form.cleaned_data['year_from']
        year_to = form.cleaned_data['year_to']
        petrol = form.cleaned_data['petrol']
        gear = form.cleaned_data['gear']
 
        car_list = scraper.scrap(mark,model,petrol,gear)
        search = form.save(commit=False)
        search.author = request.user
        search.save()
        dane.append(mark)
        dane.append(model)
        dane.append(petrol)
        dane.append(gear)
    else :
        form = SearchForm()
        
 
    return render(request, 'scrapping/search.html', {'car_list': car_list, 'form': form, 'dane': dane})