from django.urls import path
from .views import index, add, update, delete, detail

app_name = 'todo'

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('add/', add.as_view(), name='add'),
    path('update/<int:pk>/', update.as_view(), name='update'),
    path('delete/<int:pk>/', delete.as_view(), name='delete'),
    path('detail/<int:pk>/', detail.as_view(), name='detail'),
]
