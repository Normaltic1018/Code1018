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
    def clean_nick(self):
        nick = self.cleaned_data['nick']
        if Profile.objects.filter(nick=nick).exists():
            raise forms.ValidationError('NickName is Used')
        return nick

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class SignUpForm(UserCreationForm):
    username = forms.CharField(label="ID")
    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': SignUpForm,
        'profile': ProfileForm,
    }

class UserInfoMultiForm(MultiModelForm):
    form_classes = {
        'user': UserInfoForm,
        'profile': ProfileInfoForm,
    }
