from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField('タイトル', max_length=30)
    text = models.TextField('本文', max_length=300)
    date = models.DateField('作成日', default=timezone.now)
    check = models.BooleanField('チェック', default=False)

    def __str__(self):
        return self.title
