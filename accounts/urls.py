# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('mypage/', views.userinfo ,name='mypage'),
    path('userpage/<str:writer>', views.user_select_info, name='userpage'),
]
