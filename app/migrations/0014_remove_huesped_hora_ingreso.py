# Generated by Django 3.1.2 on 2022-06-09 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20220527_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='huesped',
            name='hora_ingreso',
        ),
    ]
