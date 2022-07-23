from typing import OrderedDict
from django.contrib import admin
from .models import Administrador, Cliente, DetallePedido , Proveedor, OrdenPedido, Minuta, TipoHabitacion, Habitacion, Promociones, Reserva, Factura, HabitacionReserva, Huesped, HabitacionPrecio

# Register your models here.
admin.site.site_header = 'Administración Doña Clarita'

class Administrador_Admin(admin.ModelAdmin):
    list_display = ["nombre", "apellido_paterno", "telefono", "email", "cargo"]

class Cliente_Admin(admin.ModelAdmin):
    list_display = ["rut", "nombre", "apellidos", "direccion", "telefono", "email", "nombre_empresa", "administrador_id_admin"]

class DetallePedido_Admin(admin.ModelAdmin):
    list_display = ["productos", "cantidad"]

class Proveedor_Admin(admin.ModelAdmin):
    list_display = ["tipo_proveedor", "email", "id_admin"]

class OrdenPedido_Admin(admin.ModelAdmin):
    list_display = ["administrador_id_admin", "proveedor_id_proveedor", "detalle_pedido_id_detalle"]

class Minuta_Admin(admin.ModelAdmin):
    list_display = ["tipo_servicio", "tipo_desayuno", "tipo_almuerzo", "tipo_once", "tipo_cena"]

class TipoHabitacion_Admin(admin.ModelAdmin):
    list_display = ["nombre_tipo", "descripcion", "capacidad", "precio"]

class Habitacion_Admin(admin.ModelAdmin):
    list_display = ["numero_habitacion", "tipo_habita_id_tipo_habita"]

class Promociones_Admin(admin.ModelAdmin):
    list_display = ["tipo_promocion", "desc_promocion", "descripcion"]

class Reserva_Admin(admin.ModelAdmin):
    list_display = ["nombre", "apellidos", "fecha_reserva", "email", "fecha_ingreso", "fecha_salida", "telefono_contacto", "precio_nro_habi", "tipo_habitacion", "servicio_comedor", "cliente_rut", "id_promocion"]

class Factura_Admin(admin.ModelAdmin):
    list_display = ["rut_cliente", "nombre_cliente", "apellidos_cliente", "direccion_cliente","telefono_cliente", "email_cliente", "detalle_habitaciones", "detalle_comedor", "dias_servicio", "total_a_pagar", "reserva_id_reserva"]

class HabitacionReserva_Admin(admin.ModelAdmin):
    list_display = ["habitacion_id_habitacion", "reserva_id_reserva"]

class Huesped_Admin(admin.ModelAdmin):
    list_display = ["rut", "nombre", "apellido_paterno", "apellido_materno", "reserva_id_reserva"]

class HabitacionPrecio_Admin(admin.ModelAdmin):
    list_display = ["numero_habi", "precio"]


admin.site.register(Administrador, Administrador_Admin)
admin.site.register(Cliente, Cliente_Admin)
admin.site.register(DetallePedido, DetallePedido_Admin)
admin.site.register(Proveedor, Proveedor_Admin)
admin.site.register(OrdenPedido, OrdenPedido_Admin)
admin.site.register(Minuta, Minuta_Admin)
admin.site.register(TipoHabitacion, TipoHabitacion_Admin)
admin.site.register(Habitacion, Habitacion_Admin)
admin.site.register(Promociones, Promociones_Admin)
admin.site.register(Reserva, Reserva_Admin)
admin.site.register(Factura, Factura_Admin)
admin.site.register(HabitacionReserva, HabitacionReserva_Admin)
admin.site.register(Huesped, Huesped_Admin)
admin.site.register(HabitacionPrecio, HabitacionPrecio_Admin)