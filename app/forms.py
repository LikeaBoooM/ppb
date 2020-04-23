from django import forms
from . models import Comment, NewCar, Search


class NewCarForm(forms.ModelForm):
    class Meta:
        model = NewCar
        year = forms.fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        fields = ['mark','model', 'content', 'year', 'price', 'image', 'petrol', 'gear',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]

class SearchForm(forms.ModelForm):
    class Meta:
        fields = ['mark','model', 'year_from', 'year_to', 'petrol', 'gear',]