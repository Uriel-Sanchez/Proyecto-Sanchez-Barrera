from turtle import color
from django.db import models

class Autos(models.Model):

    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    km=models.IntegerField()
    imagen= models.ImageField()
    