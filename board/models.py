from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    writer = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=100)
    post_contents = models.TextField(blank=True,help_text='Post Contents')

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.post_title

    def get_abolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

class Comment(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)
    comment_writer = models.CharField(max_length=100, null=True)
    writer_nick = models.CharField(max_length=100)

    class Meta:
        ordering = ['comment_date']
