from django.db import models
from users.models import User

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

class Viaje(models.Model):
    conductor = models.ForeignKey(User,on_delete=models.CASCADE, related_name='conductor_set')
    datetime = models.DateTimeField(blank=True, null=True, default=None)

    fecha = models.DateField(blank=True, null=True, default=None)
    hora = models.TimeField(blank=True, null=True, default=None)

    ciudad_origen = models.ForeignKey(Ciudad,on_delete=models.CASCADE, related_name='ciudad_origen_set')
    ciudad_destino = models.ForeignKey(Ciudad,on_delete=models.CASCADE, related_name='ciudad_destino_set')

    pasajeros = models.ManyToManyField(User, through='UsuarioPeticion')

    imagen_vehiculo = models.ImageField(upload_to="images/")
    descripcion = models.CharField(max_length=250)
    capacidad = models.PositiveIntegerField()
    ocupados = models.PositiveIntegerField(default=0)
    
    def get_model_fields(model):
        return model._meta.fields

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['conductor', 'datetime'], name='unique_conductor_datetime_combination'
            )
        ]

class UsuarioPeticion(models.Model):
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    esta_aceptado = models.BooleanField(null=True, default=None)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['viaje', 'user'], name='unique_viaje_user_combination'
            )
        ]