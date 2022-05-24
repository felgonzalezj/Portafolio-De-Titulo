# Generated by Django 3.1.2 on 2022-05-24 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_promociones_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.AutoField(primary_key=True, serialize=False)),
                ('rut_cliente', models.CharField(max_length=25)),
                ('nombre_cliente', models.CharField(max_length=25)),
                ('apellidos_cliente', models.CharField(max_length=40)),
                ('direccion_cliente', models.CharField(max_length=50)),
                ('telefono_cliente', models.CharField(max_length=20)),
                ('email_cliente', models.CharField(max_length=30)),
                ('detalle_habitaciones', models.CharField(max_length=100)),
                ('detalle_comedor', models.CharField(max_length=100)),
                ('dias_servicio', models.IntegerField()),
                ('total_a_pagar', models.IntegerField()),
                ('reserva_id_reserva', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.reserva')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
    ]