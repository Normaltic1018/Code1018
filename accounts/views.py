# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from .forms import ProfileForm, UserCreationMultiForm, UserInfoForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.contrib.auth.models import User

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserSignupView(generic.CreateView):
    form_class = UserCreationMultiForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form['user'].save()
        profile = form['profile'].save(commit=False)
        profile.user = user
        profile.save()
        return redirect(self.success_url)

class UserInfoView(LoginRequiredMixin, generic.DetailView):
    model = User
    #form_class = UserInfoForm
    template_name = 'mypage.html'
