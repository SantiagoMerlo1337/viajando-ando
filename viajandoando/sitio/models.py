from datetime import datetime

from operator import truediv
from platform import release
from pyexpat import model
from sys import maxsize

from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

# Create your models here.

class Provincia(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    provincia= models.ForeignKey(Provincia,on_delete=models.CASCADE)
    def __str__(self):
        string = str(self.nombre) + ', ' + str(self.provincia)
        return string

class Conductor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    licencia = models.CharField(max_length=250)

class Viaje(models.Model):
    conductor = models.ForeignKey(User,on_delete=models.CASCADE, related_name='conductor_set')
    datetime = models.DateTimeField(blank=True, null=True, default=None)

    fecha = models.DateField(blank=True, null=True, default=None)
    hora = models.TimeField(blank=True, null=True, default=None)

    imagen = models.ImageField(upload_to="images/", blank=True, null=True, default=None)

    ciudad_origen = models.ForeignKey(Ciudad,on_delete=models.CASCADE, related_name='ciudad_origen_set')
    ciudad_destino = models.ForeignKey(Ciudad,on_delete=models.CASCADE, related_name='ciudad_destino_set')

    user1 = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user1_set', blank=True, null=True, default=None)
    user2 = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user2_set', blank=True, null=True, default=None)
    
    descripcion = models.CharField(max_length=250)
    capacidad = models.PositiveIntegerField()

    def get_model_fields(model):
        return model._meta.fields

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['conductor', 'datetime'], name='unique_conductor_datetime_combination'
            )
        ]
