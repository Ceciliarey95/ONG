# Generated by Django 3.2.5 on 2022-08-15 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0004_auto_20220814_0752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='status',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
