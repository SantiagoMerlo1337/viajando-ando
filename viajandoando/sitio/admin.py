from django.contrib import admin
from sitio.models import *
# Register your models here.

@admin.register(Ciudad)
class AdminCiudad(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'provincia_id')

@admin.register(Provincia)
class AdminProvincia(admin.ModelAdmin):
    list_display = ('id', 'nombre')
