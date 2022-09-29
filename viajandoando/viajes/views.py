from tkinter.messagebox import RETRY
from django.shortcuts import render, HttpResponseRedirect
from viajes.models import *
from users.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from django.http import JsonResponse

def inicio(request):
    return render(request, 'base.html', {})

def viajes(request):
	form = ''
	viajes = ''
	origen = ''
	destino = ''
	if request.method == "GET":
		form = BuscarViajesFormulario(request.GET)
		if form.is_valid() and form.cleaned_data['fecha_inicio'] < form.cleaned_data['fecha_fin'] and form.cleaned_data['ciudad_origen'] != form.cleaned_data['ciudad_destino']:
			date1 = form.cleaned_data['fecha_inicio']
			date2 = form.cleaned_data['fecha_fin']
			origen = form.cleaned_data['ciudad_origen']
			destino = form.cleaned_data['ciudad_destino']
			viajes = Viaje.objects.filter(datetime__range=[date1, date2], ciudad_origen=origen, ciudad_destino=destino)
	return render(request, "viajes/viajes.html", {"form": form, 'lista_viajes': viajes, 'origen':origen, 'destino': destino, 'userActivo': request.user.id})

@login_required
def crear_viaje(request):
	form = CrearViajeFormulario(request.POST, request.FILES)
	prueba = False
	if Conductor.objects.filter(user=request.user).count() == 1:
		prueba = True
	if form.is_valid() and form.cleaned_data['fecha'] > date.today() and form.cleaned_data['ciudad_origen'] != form.cleaned_data['ciudad_destino'] and prueba == True:
		viaje = form.save(commit=False)
		viaje.datetime = datetime.combine(viaje.fecha, viaje.hora)
		viaje.conductor = request.user
		form.save()
		return HttpResponseRedirect("/viajes/")
	else:
		form = CrearViajeFormulario()
	return render(request, "viajes/crear.html", {"form": form})

def obtener_viaje(request, id):
	viaje = Viaje.objects.get(id=id)
	return JsonResponse({"conductor_nombre": viaje.conductor.username,"conductor": viaje.conductor.id, "descripcion": viaje.descripcion, "fecha": viaje.fecha, "hora": viaje.hora,"capacidad": viaje.capacidad, "imagen_vehiculo": str(viaje.imagen_vehiculo)})

def obtener_viajes(request):
	viajes = Viaje.objects.all().values('id', 'conductor', 'datetime', 'descripcion', 'capacidad', 'ocupados', 'ciudad_destino_id', 'ciudad_origen_id', 'conductor_id', 'imagen_vehiculo')
	viajes = list(viajes)
	return JsonResponse(viajes, safe=False)