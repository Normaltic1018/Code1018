from django.conf.urls import url #User 모델을 불러옴 // 현재는 슈퍼유저밖에없으니, 슈퍼유저 등록했던 사용자 출력
from . import views
from blog.views import *

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url('search/', SearchFormView.as_view(), name='search'),
]
