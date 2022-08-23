from django.db import models

# Create your models here.
class Usuario(models.Model):
    Username = models.CharField(max_length=25)
    Email = models.CharField(max_length=60)
    Password = models.CharField(max_length=50)
    ConfirmPassword = models.CharField(max_length=50)
    EsConductor = models.BooleanField(default=False)