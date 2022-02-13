from django.db import models
class Propietario(models.Model):

    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    email=models.EmailField()
    fechaDeAdquisicion=models.DateField()
 

