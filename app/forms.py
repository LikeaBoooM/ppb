from django import forms
from . models import Comment, NewCar


class NewCarForm(forms.ModelForm):
    class Meta:
        model = NewCar
        year = forms.fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        fields = ('mark', 'image','model', 'content', 'price', 'petrol', 'gear')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)