# board/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_index, name='board_index'),
]
