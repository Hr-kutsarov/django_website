# Generated by Django 4.1.3 on 2022-12-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_tickets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seat_number',
            field=models.IntegerField(unique=True, verbose_name='Seat Number'),
        ),
    ]