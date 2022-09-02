from msilib.schema import Class
from operator import truediv
from platform import release
from pyexpat import model
from sys import maxsize
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Provincia(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    provincia_id = models.ForeignKey(Provincia,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Conductor(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.BigIntegerField(primary_key=True)

class Viaje(models.Model):
    descripcion = models.CharField(max_length=250)
    capacidad = models.IntegerField()
    conductor = models.ForeignKey(User,on_delete=models.CASCADE)

    ciudad_id_origen = models.ForeignKey(Ciudad,on_delete=models.CASCADE, related_name='ciudad_de_origen')
    ciudad_id_destino = models.ForeignKey(Ciudad,on_delete=models.CASCADE, related_name='ciudad_de_destino')
    