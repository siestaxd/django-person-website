# Generated by Django 5.0.1 on 2024-02-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='thumb',
            field=models.ImageField(default='selammrb', upload_to='blog/', verbose_name='küçük resim'),
            preserve_default=False,
        ),
    ]