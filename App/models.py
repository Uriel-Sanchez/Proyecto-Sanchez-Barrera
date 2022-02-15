
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import User
#from django.template.defaultfilters import slugify
# Create your models here.

class Autos(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    km=models.IntegerField()
    imagen=models.ImageField(upload_to= "autos", null=True)

    def __str__(self):
        return f'{self.marca}  , {self.modelo}, {self.imagen}'
class Motos(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    km=models.IntegerField()
    imagen=models.ImageField(upload_to= "motos",  null=True)
    
    def __str__(self):
            return f'{self.marca}  ,  {self.modelo}, {self.imagen}'

class Propietario(models.Model):

    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni= models.IntegerField()
    email=models.EmailField()
    fechaDeAdquisicion=models.DateField()
    
    def __str__(self):
        return f'{self.nombre}  ,  {self.apellido}'


class Mensajeria(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destinatario = models.CharField(max_length=50)
    mensaje=models.CharField(max_length=1000)

    def __str__(self):
        return f'Mensaje de {self.user} a {self.destinatario}'

   