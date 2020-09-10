from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Todo
from .forms import CreateForm


class index(ListView):
    model = Todo
    template_name = 'todo/index.html'


class add(CreateView):
    form_class = CreateForm
    template_name = 'todo/add.html'
    success_url = reverse_lazy('todo:index')
