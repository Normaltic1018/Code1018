from django.db import models
from django.urls import reverse
from accounts.models import Profile

class Tool(models.Model):
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    tool_date = models.DateTimeField(auto_now_add=True)
    tool_title = models.CharField(max_length=100)
    tool_contents = models.TextField(blank=True,help_text='Post Contents')
    tool_like = models.PositiveIntegerField(default=0)
    tool_file = models.FileField(upload_to='tool/', null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.tool_title

    def get_abolute_url(self):
        return reverse('tool-detail', args=[str(self.id)])

    @property
    def update_counter(self):
        self.tool_like = self.tool_like + 1
        self.save()

class ToolComment(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)
    comment_writer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-id']
