# Generated by Django 5.0.1 on 2024-02-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Kısa AÇıklama'),
        ),
    ]
