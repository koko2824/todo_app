from django.shortcuts import render, redirect
from .forms import CreateForm
from .models import Todo


def index(request):
    context = {
        'todo_list': Todo.objects.all()
    }
    return render(request, 'todo/index.html', context)


def add(request):
    form = CreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('todo:index')

    context = {
        'form': CreateForm
    }
    return render(request, 'todo/add.html', context)
