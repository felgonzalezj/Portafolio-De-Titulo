import imp
from msilib.schema import Class
from multiprocessing import context
from pyexpat.errors import messages
from re import template
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from app.models import Huesped, Proveedor, Reserva
from .forms import CustomUserCreationForm, ReservaForm, HuespedForm, ProveedorForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View

import os
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.


def home(request):
    return render(request, 'app/home.html')


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


def habitaciones(request):
    return render(request, 'app/habitaciones.html')


def gastronomia(request):
    return render(request, 'app/gastronomia.html')


def reserva(request):

    data = {
        'form': ReservaForm
    }

    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(
                request, "Reserva exitosa, Porfavor registrar huespedes correspondientes")
            return redirect(to="agregar_huesped")
        else:
            data["form"] = formulario

    return render(request, 'app/reserva/agregar.html', data)


def listar_reservas(request):
    reservas = Reserva.objects.all()

    data = {
        'reservas': reservas
    }

    return render(request, 'app/reserva/listar.html', data)


def modificar_reserva(request, id):

    reserva = get_object_or_404(Reserva, id_reserva=id)

    data = {
        'form': ReservaForm(instance=reserva)
    }

    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST, instance=reserva)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Reserva modificada!")
            return redirect(to="listar_reservas")
        data["form"] = formulario

    return render(request, 'app/reserva/modificar.html', data)


def eliminar_reserva(request, id):

    reserva = get_object_or_404(Reserva, id_reserva=id)
    reserva.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_reservas")


class reserva_pdf(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('app/reserva/pdf.html')
            reservas = Reserva.objects.all()
            context = {
                'reservas': reservas
            }
            html = template.render(context)
            response = HttpResponse(content_type='')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('listar-reservas'))


def agregar_huesped(request):

    data = {
        'form': HuespedForm
    }

    if request.method == 'POST':
        formulario = HuespedForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Huesped agregado")
        else:
            data["form"] = formulario

    return render(request, 'app/huesped/agregar.html', data)


def listar_huesped(request):

    huesped = Huesped.objects.all()

    data = {
        'huesped': huesped
    }

    return render(request, 'app/huesped/listar.html', data)


def modificar_huesped(request, id):

    huesped = get_object_or_404(Huesped, rut=id)

    data = {
        'form': HuespedForm(instance=huesped)
    }

    if request.method == 'POST':
        formulario = HuespedForm(data=request.POST, instance=huesped)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Huesped modificado!")
            return redirect(to="listar_huesped")
        data["form"] = formulario

    return render(request, 'app/huesped/modificar.html', data)


def eliminar_huesped(request, id):

    reserva = get_object_or_404(Huesped, rut=id)
    reserva.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_huesped")


def agregar_proveedor(request):

    data = {
        'form': ProveedorForm()
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor agregado")
        else:
            data["form"] = formulario

    return render(request, 'app/proveedores/agregar.html', data)


def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    data = {
        'proveedores': proveedores
    }

    return render(request, 'app/proveedores/listar.html', data)


def modificar_proveedor(request, id):

    proveedor = get_object_or_404(Proveedor, id_proveedor=id)

    data = {
        'form': ProveedorForm(instance=proveedor)
    }

    if request.method == 'POST':
        formulario = ProveedorForm(
            data=request.POST, instance=proveedor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_proveedores")
        data["form"] = formulario

    return render(request, 'app/proveedores/modificar.html', data)


def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    proveedor.delete()
    messages.success(request, "Proveedor eliminado")
    return redirect(to="listar_proveedores")
