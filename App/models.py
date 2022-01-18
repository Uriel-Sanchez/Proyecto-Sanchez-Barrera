from django.db import models

# Create your models here.

class Autos(models.Model):

    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    km=models.IntegerField()

    def __str__(self):
        return f'{self.marca}-{self.modelo}'

class Motos(models.Model):

    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    km=models.IntegerField()

class Propietario(models.Model):

    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    fechaDeAdquisicion=models.DateField()