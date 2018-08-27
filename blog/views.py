from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q # 검색기능에 필요한 q 클래스를 import
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from accounts.models import Profile

class PostListView(generic.ListView):
    model = Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "GET":
        form = PostForm(request.POST)
    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            conn_profile = Profile.objects.get(user=request.user)
            post = form.save(commit=False)
            post.author = conn_profile
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(instance=post)
        conn_profile = Profile.objects.get(user=request.user)

        if conn_profile != post.writer:
            messages.info(request, 'You are not allowed')
            return render(request, 'blog/post_edit.html',context=context )

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.info(request, 'Successfully Modified!')
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    conn_profile = Profile.objects.get(user=request.user)

    if conn_profile != post.writer:
        messages.info(request, 'You are not allowed')
        return render(request, 'blog/post_detail.html',context=context )

    post.delete()
    return redirect('blog:post_list')

class SearchFormView(generic.FormView):
    # form_class를 forms.py에서 정의했던 PostSearchForm으로 정의
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    # 제출된 값이 유효성검사를 통과하면 form_valid 메소드 실행
    # 여기선 제출된 search_word가 PostSearchForm에서 정의한대로 Char인지 검사
    def form_valid(self, form):
        # 제출된 값은 POST로 전달됨
        # 사용자가 입력한 검색 단어를 변수에 저장
        search_word = self.request.POST['search_word']
        # Post의 객체중 제목이나 설명이나 내용에 해당 단어가 대소문자관계없이(icontains) 속해있는 객체를 필터링
        post_list = Post.objects.filter(Q(title__icontains=search_word) |
                                        Q(text__icontains=search_word)
                                        )

        context = {}
        # context에 form객체, 즉 PostSearchForm객체 저장
        context['form'] = form
        context['search_term'] = search_word
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)
