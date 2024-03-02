# Generated by Django 5.0.1 on 2024-01-28 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socialmedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Sosyal Medya Adı')),
                ('icon_paket_link', models.TextField(verbose_name='kullanilacak olan icon paketinin linki')),
                ('icon', models.CharField(max_length=200, verbose_name='Sosyal Medya İkonu')),
                ('link', models.CharField(max_length=200, verbose_name='Sosyal Medya Linki')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name': 'Sosyal Medya',
                'verbose_name_plural': 'Sosyal Medya',
            },
        ),
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Profil Başlığı')),
                ('description', models.TextField(verbose_name='Profil Açıklaması')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Profil Resmi')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('socialmedia', models.ManyToManyField(to='main.socialmedia', verbose_name='Sosyal Medya Hesapları')),
            ],
            options={
                'verbose_name': 'Anasayfa',
                'verbose_name_plural': 'Anasayfa',
            },
        ),
    ]