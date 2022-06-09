from unicodedata import name
from django.urls import path
from .views import home, proveedores, reserva, registro, habitaciones, gastronomia, listar_reservas, modificar_reserva, eliminar_reserva, reserva_pdf, agregar_huesped , listar_huesped, modificar_huesped, eliminar_huesped

urlpatterns = [
    path('', home, name="home"),
    path('proveedores/', proveedores, name="proveedores"),
    path('reserva/', reserva, name="reserva"),
    path('registro/', registro, name="registro"),
    path('habitaciones/', habitaciones, name="habitaciones"),
    path('gastronomia/', gastronomia, name="gastronomia"),
    path('listar-reservas/', listar_reservas, name="listar_reservas"),
    path('modificar-reserva/<id>/', modificar_reserva, name="modificar_reserva"),
    path('eliminar-reserva/<id>/', eliminar_reserva, name="eliminar_reserva"),
    path('reserva-pdf/', reserva_pdf.as_view(), name="reserva_pdf"),
    path('agregar-huesped/', agregar_huesped, name="agregar_huesped"),
    path('listar-huesped/', listar_huesped, name="listar_huesped"),
    path('modificar-huesped/<id>/', modificar_huesped, name="modificar_huesped"),
    path('eliminar-huesped/<id>/', eliminar_huesped, name="eliminar_huesped"),
]
