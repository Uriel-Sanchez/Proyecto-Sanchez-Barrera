from cProfile import label
from dataclasses import fields
from socket import fromshare
from tkinter.tix import Form
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import template

class Formulario_auto(forms.Form):

    marca=forms.CharField()
    modelo=forms.CharField()
    color=forms.CharField()
    km=forms.IntegerField()
    imagen=forms.ImageField()


class Formulario_moto(forms.Form):
    marca=forms.CharField()
    modelo=forms.CharField()
    color=forms.CharField()
    km=forms.IntegerField()
    imagen=forms.ImageField()


class Formulario_propietario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()
    fechaDeAdquisicion=forms.DateField()


class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    

class Meta:
    model = User
    fields = ['email', 'password1', 'password1','first_name','last_name']

    
