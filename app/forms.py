from django import forms
from . models import Comment, NewCar


class NewCarForm(forms.ModelForm):
    class Meta:
        model = NewCar
        fields = ('mark', 'image', 'content',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)