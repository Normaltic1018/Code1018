from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm
from accounts.models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
import datetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

def get_nick(user):
    conn_user = user
    conn_profile = Profile.objects.get(user=conn_user)
    nick = conn_profile.nick
    return nick

# Create your views here.
class PostListView(generic.ListView):
    model = Post
    paginate_by = 10

class PostDetailView(generic.DetailView):
    model = Post

@login_required
def post_write(request):
    # save process
    if request.method == 'POST':
        form = CreatePostForm(request.POST)

        if form.is_valid():
            conn_user = request.user
            conn_profile = Profile.objects.get(user=conn_user)
            nick = conn_profile.nick
            #new_post = Post()
            new_post = form.save(commit=False)
            new_post.writer = nick
            new_post.save()
            messages.info(request, 'Successfully Post!')
            return HttpResponseRedirect(reverse_lazy('board_index'))
    # send form
    else:
        form = CreatePostForm()

    return render(request, 'board/write_post.html', {'form': form})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk = pk)
    context = {'post' : post,}
    # save process
    if request.method == 'POST':
        form = CreatePostForm(request.POST, instance=post)
        conn_user = request.user
        nick = get_nick(conn_user)

        if nick != post.writer:
            messages.info(request, 'You are not allowed')
            return render(request, 'board/post_detail.html',context=context )

        if form.is_valid():
            post = form.save(commit=False)
            post.post_date = datetime.datetime.now()
            post.save()
            messages.info(request, 'Successfully Modified!')
            return render(request, 'board/post_detail.html',context=context )
    # send form
    else:
        title = post.post_title
        content = post.post_contents
        form = CreatePostForm(initial={'post_title': title,'post_contents':content,})

    return render(request, 'board/write_post.html', {'form': form})

@login_required
def comment_write(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        context = {'post' : post,}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = Profile.objects.get(user=conn_user)

        if not content:
            messages.info(request, 'You dont write anything....')
            return render(request, 'board/post_detail.html',context=context )

        Comment.objects.create(post=post, comment_writer=conn_profile,comment_contents=content)
        return render(request, 'board/post_detail.html',context=context )


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('board_index')

    def get_queryset(self):
        conn_user = self.request.user
        nick = get_nick(conn_user)
        return self.model.objects.filter(writer=nick)

@login_required
def comment_delete(request, post_pk, pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_object_or_404(Comment, pk=pk)

    context = {'post' : post,}
    content = request.POST.get('content')

    conn_user = request.user
    conn_profile = Profile.objects.get(user=conn_user)

    if conn_profile != comment.comment_writer:
        messages.info(request, 'You are not allowed....')
        return render(request, 'board/post_detail.html',context=context )

    comment.delete()
    return render(request, 'board/post_detail.html',context=context )
