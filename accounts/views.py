# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from .forms import ProfileForm, UserCreationMultiForm, UserInfoForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User
from .models import Profile

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

@login_required
def userinfo(request):
    conn_user = request.user
    conn_profile = Profile.objects.get(user=conn_user)
    level_dict = dict(Profile.LEVEL)

    if not conn_profile.profile_image:
        pic_url = ""
    else:
        pic_url = conn_profile.profile_image.url

    context = {
        'id' : conn_user.username,
        'first_name' : conn_user.first_name,
        'last_name' : conn_user.last_name,
        'nick' : conn_profile.nick,
        'level' : level_dict[conn_profile.level],
        'birth_date' : conn_profile.birth_date,
        'profile_pic' : pic_url,
        'intro' : conn_profile.intro,
    }
    return render(request, 'mypage.html', context=context)
