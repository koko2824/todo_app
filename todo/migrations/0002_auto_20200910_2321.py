# Generated by Django 3.0.8 on 2020-09-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.TextField(max_length=300, verbose_name='本文'),
        ),
    ]
