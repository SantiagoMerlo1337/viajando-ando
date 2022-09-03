from msilib.schema import Class
from operator import truediv
from platform import release
from pyexpat import model
from sys import maxsize
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Provincia(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    provincia= models.ForeignKey(Provincia,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Conductor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    licencia = models.CharField(max_length=250)

class Viaje(models.Model):
    conductor = models.ForeignKey(User,on_delete=models.CASCADE, related_name='conductor_set')
    fecha = models.DateTimeField(default=timezone.now())

    ciudad_origen = models.ForeignKey(Ciudad,on_delete=models.CASCADE, related_name='ciudad_origen_set')
    ciudad_destino = models.ForeignKey(Ciudad,on_delete=models.CASCADE, related_name='ciudad_destino_set')

    user1 = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user1_set')
    user2 = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user2_set')
    
    descripcion = models.CharField(max_length=250)
    capacidad = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['conductor', 'fecha'], name='unique_conductor_fecha_combination'
            )
        ]
    
#, blank=True, null=True