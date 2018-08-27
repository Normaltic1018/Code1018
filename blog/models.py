from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from accounts.models import Profile

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='%Y/%m/%d/orig', blank=True, null=True) #원본 사진파일

    class Meta:
        ordering = ['-id']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Post, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        url = reverse_lazy('blog:post_detail', kwargs={'pk': self.pk})
        return url
