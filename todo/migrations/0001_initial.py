# Generated by Django 3.0.8 on 2020-09-09 04:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='タイトル')),
                ('text', models.CharField(max_length=300, verbose_name='本文')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('check', models.BooleanField(default=False, verbose_name='チェック')),
            ],
        ),
    ]
