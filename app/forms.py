from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username',"first_name","last_name","email","password1","password2"]
