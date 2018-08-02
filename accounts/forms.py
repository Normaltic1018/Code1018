from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from django.conf import settings
from django.contrib.auth.models import User
from betterforms.multiform import MultiModelForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nick','birth_date',]

class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': UserCreationForm,
        'profile': ProfileForm,
    }
