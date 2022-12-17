# Generated by Django 4.1.3 on 2022-12-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_news_options_alter_artist_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.CharField(max_length=400, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='first_name',
            field=models.CharField(max_length=15, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(max_length=15, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=30, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='play',
            name='genre',
            field=models.CharField(max_length=15, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='play',
            name='title',
            field=models.CharField(max_length=30, unique=True, verbose_name='Title'),
        ),
    ]