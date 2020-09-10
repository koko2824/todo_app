from django.urls import path
from .views import index, add

app_name = 'todo'

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('add/', add.as_view(), name='add'),
]
