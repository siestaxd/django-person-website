# Generated by Django 5.0.1 on 2024-01-30 05:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_about_job_about_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='içerik'),
        ),
    ]
