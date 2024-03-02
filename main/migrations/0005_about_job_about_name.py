# Generated by Django 5.0.1 on 2024-01-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_skills_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='job',
            field=models.CharField(default='junior developer', max_length=200, verbose_name='Meslek'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='name',
            field=models.CharField(default='hamza bilen', max_length=200, verbose_name='Ad Soyad'),
            preserve_default=False,
        ),
    ]
