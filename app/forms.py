from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reserva, Huesped

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]


class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'

        widgets = {
            "fecha_reserva" : forms.SelectDateWidget(),
            "fecha_ingreso" : forms.SelectDateWidget(),
            "fecha_salida" : forms.SelectDateWidget()
        }


class HuespedForm(forms.ModelForm):

    class Meta:
        model = Huesped
        fields = '__all__'

        widgets = {
            "fecha_reserva" : forms.SelectDateWidget(),
            "fecha_ingreso" : forms.SelectDateWidget(),
            "fecha_salida" : forms.SelectDateWidget()
        }