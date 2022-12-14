# Generated by Django 4.1.3 on 2022-12-16 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.TimeField(default=datetime.datetime.now, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='play',
            name='price',
            field=models.CharField(max_length=10, verbose_name='Price'),
        ),
    ]
