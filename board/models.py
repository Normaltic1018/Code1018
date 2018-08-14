from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Profile

class Post(models.Model):
    writer = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=100)
    post_contents = models.TextField(blank=True,help_text='Post Contents')
    post_hit = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.post_title

    def get_abolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    @property
    def update_counter(self):
        self.post_hit = self.post_hit + 1
        self.save()

    @property
    def is_auth(self, nick):
        if writer != nick:
            return False
        else:
            return True

class Comment(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)
    comment_writer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-id']
