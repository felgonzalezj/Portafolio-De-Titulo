# Generated by Django 3.1.2 on 2022-05-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20220527_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacionprecio',
            name='numero_habi',
            field=models.CharField(max_length=50),
        ),
    ]