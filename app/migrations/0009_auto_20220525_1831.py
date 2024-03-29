# Generated by Django 3.1.2 on 2022-05-25 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_habitacionreserva_huesped'),
    ]

    operations = [
        migrations.CreateModel(
            name='HabitacionPrecio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_habi', models.CharField(max_length=20)),
                ('precio', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Nro habitaciones - Precio',
                'verbose_name_plural': 'Nro habitaciones - Precio',
            },
        ),
        migrations.AlterField(
            model_name='reserva',
            name='precio_nro_habi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.habitacionprecio'),
        ),
    ]
