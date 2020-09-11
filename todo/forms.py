from django import forms
from .models import Todo


class CreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'text', 'check')
