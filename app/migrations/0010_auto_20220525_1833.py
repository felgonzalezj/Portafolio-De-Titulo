# Generated by Django 3.1.2 on 2022-05-25 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20220525_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='precio_nro_habi',
            field=models.IntegerField(choices=[[0, '1 habitacion - $20.000'], [1, '2 habitacion - $40.000'], [2, '3 habitacion - $60.000'], [3, '4 habitacion - $80.000'], [4, '5 habitacion - $100.000'], [5, '6 habitacion - $120.000']]),
        ),
        migrations.DeleteModel(
            name='HabitacionPrecio',
        ),
    ]
