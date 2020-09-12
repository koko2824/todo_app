from django.views import generic
from django.urls import reverse_lazy
from .models import Todo
from .forms import CreateForm


class index(generic.ListView):
    paginate_by = 15
    model = Todo
    template_name = 'todo/index.html'


class add(generic.CreateView):
    model = Todo
    form_class = CreateForm
    template_name = 'todo/add.html'
    success_url = reverse_lazy('todo:index')


class update(generic.UpdateView):
    model = Todo
    form_class = CreateForm
    template_name = 'todo/update.html'
    success_url = reverse_lazy('todo:index')


class delete(generic.DeleteView):
    model = Todo
    form_class = CreateForm
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('todo:index')


class detail(generic.DetailView):
    model = Todo
    template_name = 'todo/detail.html'
