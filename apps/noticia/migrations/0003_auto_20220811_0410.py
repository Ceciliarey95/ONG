# Generated by Django 3.2.5 on 2022-08-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0002_auto_20220810_2140'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coment',
            new_name='Comment',
        ),
        migrations.AlterField(
            model_name='noticia',
            name='slug',
            field=models.SlugField(max_length=250, unique=True, unique_for_date='published'),
        ),
    ]