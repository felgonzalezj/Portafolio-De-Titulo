from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404

from app.models import Reserva
from .forms import CustomUserCreationForm, ReservaForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def proveedores(request):
    return render(request, 'app/proveedores.html')

def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario =  CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            #messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def habitaciones(request):
    return render(request, 'app/habitaciones.html')

def gastronomia(request):
    return render(request, 'app/gastronomia.html')

def reserva(request):

    data = {
        'form' : ReservaForm
    }

    if request.method == 'POST':
        formulario =  ReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Reserva exitosa"
        else:
            data["form"] = formulario

    return render(request, 'app/reserva/agregar.html', data)


def listar_reservas(request):
    reservas = Reserva.objects.all()

    data = {
        'reservas' : reservas
    }

    return render(request, 'app/reserva/listar.html', data)


def modificar_reserva(request, id):

    reserva = get_object_or_404(Reserva, id_reserva = id)

    data = {
        'form': ReservaForm(instance=reserva)
    }

    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST, instance=reserva)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_reservas")
        data["form"] = formulario
 
    return render(request, 'app/reserva/modificar.html', data)


def eliminar_reserva(request, id):

    reserva = get_object_or_404(Reserva, id_reserva = id)
    reserva.delete()
    return redirect(to="listar_reservas")