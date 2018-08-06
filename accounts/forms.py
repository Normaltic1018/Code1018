from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from betterforms.multiform import MultiModelForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nick','birth_date', 'profile_image','intro',]
        widgets = {
            'birth_date': DateInput(),
        }

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': UserCreationForm,
        'profile': ProfileForm,
    }

class UserInfoMultiForm(MultiModelForm):
    form_classes = {
        'user': UserInfoForm,
        'profile': ProfileInfoForm,
    }
