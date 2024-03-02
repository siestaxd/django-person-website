# Generated by Django 5.0.1 on 2024-02-12 13:00

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Başlık')),
                ('description', models.CharField(max_length=500, verbose_name='Başlık')),
                ('content', ckeditor.fields.RichTextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Taslak'), ('published', 'Yayınlandı'), ('deleted', 'Silindi')], default='draft', max_length=10)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
            options={
                'verbose_name': 'Gönderi',
                'verbose_name_plural': 'Gönderiler',
                'ordering': ['-create_date'],
            },
        ),
    ]
