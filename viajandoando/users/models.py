from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Conductor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    licencia = models.CharField(max_length=250)
    foto_perfil = models.ImageField(upload_to="images/")

    def __str__(self):
        string = str(self.user.username)
        return string