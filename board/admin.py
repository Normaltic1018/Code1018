from django.contrib import admin
from .models import Post, Comment

class CommentsInline(admin.TabularInline):
    model = Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'writer', 'post_date')
    inlines = [CommentsInline]
# Register your models here.
