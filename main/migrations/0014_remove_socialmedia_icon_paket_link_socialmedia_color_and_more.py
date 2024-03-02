# Generated by Django 5.0.1 on 2024-02-23 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_website_settings_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialmedia',
            name='icon_paket_link',
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='color',
            field=models.CharField(default='white', max_length=50, verbose_name='Renk'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='link',
            field=models.URLField(verbose_name='Sosyal Medya Linki'),
        ),
    ]