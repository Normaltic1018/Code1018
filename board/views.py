from django.shortcuts import render

# Create your views here.
def board_index(request):
    return render(request, 'board_index.html')
