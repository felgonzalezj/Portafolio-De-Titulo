from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def reserva(request):
    return render(request, 'app/reserva.html')

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