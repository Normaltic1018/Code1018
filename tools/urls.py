# board/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToolListView.as_view(), name='tool_index'),
    path('<int:pk>', views.ToolDetailView.as_view(), name='tool-detail'),
    path('write', views.tool_write, name="tool_write"),
    path('update/<int:pk>', views.tool_update, name="tool_update"),
    path('<int:tool_pk>/comment/write', views.comment_write, name='tool_comment_write'),
    path('delete/<int:pk>', views.ToolDeleteView.as_view(), name='tool-delete'),
    path('<int:tool_pk>/comment/delete/<int:pk>', views.comment_delete, name='tool_comment_delete'),
    path('download/<int:pk>', views.tool_download,name='tool_download'),
    path('<int:tool_pk>/like-toggle', views.post_like_toggle, name='like-toggle'),
]
