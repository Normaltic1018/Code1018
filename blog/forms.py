from django import forms
from .models import Post
from django.forms import ModelForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image',)

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
