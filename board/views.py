from django.shortcuts import render
from .models import Post, Comment
from django.views import generic

# Create your views here.
class AllPostListView(generic.ListView):
    model = Post

def board_index(request):

    return render(request, 'board_index.html')

class AllLoanedBooksListView(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    permission_required = 'catalog.can_mark_returned'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')
