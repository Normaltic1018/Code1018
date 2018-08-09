from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    writer = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=100)
    post_contents = models.TextField(blank=True,help_text='Post Contents')

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return post_title

class Comment(models.Model):
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)
    comment_write = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    writer_nick = models.CharField(max_length=100)

    class Meta:
        ordering = ['comment_date']
