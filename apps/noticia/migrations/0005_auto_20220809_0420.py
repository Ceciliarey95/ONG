# Generated by Django 3.2.5 on 2022-08-09 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0004_auto_20220808_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='likes',
        ),
        migrations.AddField(
            model_name='noticia',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
