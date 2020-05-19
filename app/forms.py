from django import forms
from . models import Comment, NewCar, Search, Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        

class NewCarForm(forms.ModelForm):
    class Meta:
        model = NewCar
        year = forms.fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        fields = ['mark','model', 'content','link', 'year', 'price', 'image', 'petrol', 'gear',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['mark','model', 'year_from', 'year_to', 'petrol', 'gear',]