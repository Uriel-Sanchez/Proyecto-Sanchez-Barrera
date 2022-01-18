from django.db import models


class Motos(models.Model):

    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    km=models.IntegerField()