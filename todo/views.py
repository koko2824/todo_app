from django.views import generic
from django.urls import reverse_lazy
from .models import Todo
from .forms import CreateForm


class index(generic.ListView):
    model = Todo
    template_name = 'todo/index.html'


class add(generic.CreateView):
    form_class = CreateForm
    template_name = 'todo/add.html'
    success_url = reverse_lazy('todo:index')


class update(generic.UpdateView):
    pass


class delete(generic.DeleteView):
    pass


class detail(generic.DetailView):
    pass
