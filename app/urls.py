from unicodedata import name
from django.urls import path
from .views import home, proveedores, reserva, registro, habitaciones, gastronomia

urlpatterns = [
    path('', home, name="home"),
    path('proveedores/', proveedores, name="proveedores"),
    path('reserva/', reserva, name="reserva"),
    path('registro/', registro, name="registro"),
    path('habitaciones/', habitaciones, name="habitaciones"),
    path('gastronomia/', gastronomia, name="gastronomia"),
]
