from django import forms
from .models import Tool

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['tool_title','tool_contents', 'tool_file']

class ModifyToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['tool_title','tool_contents',]
