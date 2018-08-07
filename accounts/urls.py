# accounts/urls.py

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('mypage/', views.userinfo ,name='mypage'),
]
