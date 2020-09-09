from django.shortcuts import render
from .forms import CreateForm


def index(request):
    return render(request, 'todo/index.html')


def add(request):
    context = {
        'form': CreateForm
    }
    return render(request, 'todo/add.html', context)
