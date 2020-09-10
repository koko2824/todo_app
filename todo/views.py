from django.views.generic import FormView, ListView
from .models import Todo
from .forms import CreateForm


class index(ListView):
    model = Todo
    template_name = 'todo/index.html'


class add(FormView):
    form_class = CreateForm
    template_name = 'todo/add.html'
