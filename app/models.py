from django.db import models

# Create your models here.

class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    cargo = models.CharField(max_length=30)
    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

    def __str__(self) :
        return self.nombre + '  ' + self.apellido_paterno


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    direccion = models.CharField(max_length=35)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=40)
    nombre_empresa = models.CharField(max_length=30)
    rut_empresa = models.CharField(max_length=40)
    direccion_empresa = models.CharField(max_length=40)
    administrador_id_admin = models.ForeignKey(Administrador, on_delete=models.PROTECT)
    class Meta: 
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self) :
        return self.nombre + '  ' + self.apellidos


class DetallePedido(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    productos = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    class Meta:
        verbose_name = "Detalle Pedido"
        verbose_name_plural = "Detalle Pedidos"

    def __str__(self) :
        return self.productos

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    tipo_proveedor = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    id_admin = models.ForeignKey(Administrador, on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self) :
        return self.tipo_proveedor

class OrdenPedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    administrador_id_admin = models.ForeignKey(Administrador, on_delete=models.PROTECT)
    proveedor_id_proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    detalle_pedido_id_detalle = models.ForeignKey(DetallePedido, on_delete=models.PROTECT)
    class Meta:       
        verbose_name = "Orden Pedido"
        verbose_name_plural = "Ordenes Pedidos"

    def __int__(self) :
        return self.proveedor_id_proveedor + '  ' + self.detalle_pedido_id_detalle


class Minuta(models.Model):
    id_minuta = models.AutoField(primary_key=True)
    tipo_servicio = models.CharField(max_length=50)
    tipo_desayuno = models.CharField(max_length=50)
    tipo_almuerzo = models.CharField(max_length=50)
    tipo_once = models.CharField(max_length=50)
    tipo_cena = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Minuta"
        verbose_name_plural = "Minuta"

    def __str__(self) :
        return self.tipo_servicio


class TipoHabitacion(models.Model):
    id_tipo_habitacion = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio = models.IntegerField()
    class Meta:
        verbose_name = "Tipo Habitacion"
        verbose_name_plural = "Tipo Habitaciones"

    def __str__(self) :
        return self.nombre_tipo


class Habitacion(models.Model):
    id_habitacion = models.AutoField(primary_key=True)
    numero_habitacion = models.CharField(max_length=20)
    tipo_habita_id_tipo_habita = models.ForeignKey(TipoHabitacion, models.PROTECT)
    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    def __str__(self) :
        return self.numero_habitacion


class Promociones(models.Model):
    id_promociones = models.AutoField(primary_key=True)
    tipo_promocion = models.CharField(max_length=50)
    desc_promocion = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Promocion"
        verbose_name_plural = "Promociones"
        
    def __str__(self) :
        return self.tipo_promocion + '  ' + self.desc_promocion


class HabitacionPrecio(models.Model):
    id = models.AutoField(primary_key=True)
    numero_habi = models.CharField(max_length=50)
    precio = models.CharField(max_length=20)
    class Meta:
        verbose_name = "Nro habitaciones - Precio"
        verbose_name_plural = "Nro habitaciones - Precio"

    def __str__(self) :
        return self.numero_habi + ' - ' + self.precio


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    fecha_reserva = models.DateField()
    email = models.CharField(max_length=40)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    telefono_contacto = models.CharField(max_length=15) 
    precio_nro_habi = models.ForeignKey(HabitacionPrecio, models.PROTECT)
    tipo_habitacion = models.ForeignKey(TipoHabitacion, models.PROTECT)
    servicio_comedor = models.ForeignKey(Minuta, models.PROTECT)
    cliente_rut = models.ForeignKey(Cliente, models.PROTECT)
    id_promocion = models.ForeignKey(Promociones, models.PROTECT)
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self) :
        return self.nombre + '  ' + self.apellidos


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    rut_cliente = models.CharField(max_length=25)
    nombre_cliente = models.CharField(max_length=25)
    apellidos_cliente = models.CharField(max_length=40)
    direccion_cliente = models.CharField(max_length=50)
    telefono_cliente = models.CharField(max_length=20)
    email_cliente = models.CharField(max_length=40)
    detalle_habitaciones = models.CharField(max_length=100)
    detalle_comedor = models.CharField(max_length=100)
    dias_servicio = models.IntegerField()
    total_a_pagar = models.IntegerField()
    reserva_id_reserva = models.ForeignKey(Reserva, models.PROTECT)
    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self) :
        return self.rut_cliente + '  ' + self.nombre_cliente + '  ' + self.apellidos_cliente


class HabitacionReserva(models.Model):
    id_habitacion_reserva = models.AutoField(primary_key=True)
    habitacion_id_habitacion = models.ForeignKey(Habitacion, models.PROTECT)
    reserva_id_reserva = models.ForeignKey(Reserva, models.PROTECT)
    class Meta:
        verbose_name = "Habitacion - Reserva"
        verbose_name_plural = "Habitacion - Reserva"

    def __int__(self) :
        return self.habitacion_id_habitacion + '  ' + self.reserva_id_reserva


class Huesped(models.Model):
    rut = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    fecha_reserva = models.DateField()
    hora_ingreso = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    reserva_id_reserva = models.ForeignKey(Reserva, models.PROTECT)
    class Meta:
        verbose_name = "Huesped"
        verbose_name_plural = "Huespedes"

    def __str__(self) :
        return self.rut + '  ' + self.nombre + '  ' +  self.apellido_paterno