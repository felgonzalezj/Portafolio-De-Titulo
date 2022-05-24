from django.contrib import admin
from .models import Administrador, Cliente, DetallePedido , Proveedor, OrdenPedido, Minuta, TipoHabitacion, Habitacion, Promociones, Reserva, Factura, HabitacionReserva, Huesped

# Register your models here.
admin.site.site_header = 'Administración Doña Clarita'

admin.site.register(Administrador)
admin.site.register(Cliente)
admin.site.register(DetallePedido)
admin.site.register(Proveedor)
admin.site.register(OrdenPedido)
admin.site.register(Minuta)
admin.site.register(TipoHabitacion)
admin.site.register(Habitacion)
admin.site.register(Promociones)
admin.site.register(Reserva)
admin.site.register(Factura)
admin.site.register(HabitacionReserva)
admin.site.register(Huesped)