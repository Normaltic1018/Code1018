from django import forms
from .models import Post, Comment
from betterforms.multiform import MultiModelForm
from django.contrib.auth.models import User

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title','post_contents',]
