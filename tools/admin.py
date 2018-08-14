from django.contrib import admin
from .models import Tool

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('tool_title', 'writer', 'tool_date')
# Register your models here.
