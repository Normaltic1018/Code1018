# board/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='board_index'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/write', views.post_write, name="post_write"),
]
