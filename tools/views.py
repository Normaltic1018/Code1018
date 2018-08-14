from django.shortcuts import render, get_object_or_404
from .models import Tool, ToolComment
from django.views import generic
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
import datetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UploadFileForm, ModifyToolForm
import os
from django.conf import settings
from django.http import HttpResponse, Http404

def get_nick(user):
    conn_user = user
    conn_profile = Profile.objects.get(user=conn_user)
    nick = conn_profile.nick
    return nick

# Create your views here.
class ToolListView(generic.ListView):
    model = Tool
    paginate_by = 10

class ToolDetailView(generic.DetailView):
    model = Tool

@login_required
def tool_write(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            conn_profile = Profile.objects.get(user=request.user)
            new_tool = form.save(commit=False)
            new_tool.writer = conn_profile
            new_tool.save()
            return HttpResponseRedirect(reverse_lazy('tool_index'))
    else:
        form = UploadFileForm()
    return render(request, 'tools/write_tool.html', {'form': form})

@login_required
def tool_update(request, pk):
    tool = get_object_or_404(Post, pk = pk)
    context = {'tool' : tool,}
    # save process
    if request.method == 'POST':
        form = ModifyToolForm(request.POST, instance=tool)
        conn_user = request.user

        if request.user != tool.writer:
            messages.info(request, 'You are not allowed')
            return render(request, 'tools/tool_detail.html',context=context )

        if form.is_valid():
            tool = form.save(commit=False)
            tool.tool_date = datetime.datetime.now()
            post.save()
            messages.info(request, 'Successfully Modified!')
            return render(request, 'tools/tool_detail.html',context=context )
    # send form
    else:
        title = tool.tool_title
        content = tool.tool_contents
        form = ModifyToolForm(initial={'tool_title': title,'tool_contents':content,})

    return render(request, 'tools/tool_detail.html',context=context )

@login_required
def comment_write(request, post_pk):
    if request.method == 'POST':
        tool = get_object_or_404(Tool, pk=tool_pk)
        context = {'tool' : tool,}
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = Profile.objects.get(user=conn_user)

        if not content:
            messages.info(request, 'You dont write anything....')
            return render(request, 'tools/tool_detail.html',context=context )

        ToolComment.objects.create(tool=tool, comment_writer=conn_profile,comment_contents=content)
        return render(request, 'tools/tool_detail.html',context=context )


class ToolDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tool
    success_url = reverse_lazy('tool_index')

    def get_queryset(self):
        conn_user = self.request.user
        return self.model.objects.filter(writer=conn_user)

@login_required
def comment_delete(request, post_pk, pk):
    tool = get_object_or_404(Tool, pk=tool_pk)
    comment = get_object_or_404(ToolComment, pk=pk)

    context = {'tool' : tool,}
    content = request.POST.get('content')

    conn_user = request.user
    conn_profile = Profile.objects.get(user=conn_user)

    if conn_profile != comment.comment_writer:
        messages.info(request, 'You are not allowed....')
        return render(request, 'tools/tool_detail.html',context=context )

    comment.delete()
    return render(request, 'tools/tool_detail.html',context=context )


@login_required
def tool_download(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    file_url = tool.tool_file.url
    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_url)
            return response
    raise Http404
