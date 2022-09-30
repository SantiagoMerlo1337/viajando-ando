from mimetypes import common_types
from tkinter.messagebox import RETRY
from django.shortcuts import render, HttpResponseRedirect
from django.urls import is_valid_path
from viajes.models import *
from users.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from django.http import JsonResponse
from django.contrib import messages

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
	else:
		form = CrearUsuarioPeticionFormulario(request.POST, request.FILES)
		if form.is_valid():
			cd = form.cleaned_data
			viaje = Viaje.objects.get(pk=cd['viaje'])
			pc = UsuarioPeticion(
                viaje = viaje,
                user = request.user
            )
			if UsuarioPeticion.objects.filter(user=request.user, viaje=viaje).count() == 0:
				pc.save()
			else:
				messages.error(request, 'Ya solicitaste unirte a este viaje.')
			return HttpResponseRedirect("/viajes")
	return render(request, "viajes/viajes.html", {"form": form, 'lista_viajes': viajes, 'origen':origen, 'destino': destino})

@login_required
def crear_viaje(request):
	form = CrearViajeFormulario(request.POST, request.FILES)
	prueba = False
	if Conductor.objects.filter(user_id=request.user).count() == 1:
		prueba = True
	if form.is_valid() and form.cleaned_data['fecha'] >= date.today() and form.cleaned_data['ciudad_origen'] != form.cleaned_data['ciudad_destino'] and prueba == True:
		viaje = form.save(commit=False)
		viaje.datetime = datetime.combine(viaje.fecha, viaje.hora)
		conductor = Conductor.objects.get(user_id=request.user.id)
		viaje.conductor = conductor
		form.save()
		return HttpResponseRedirect("/viajes/")
	else:
		form = CrearViajeFormulario()
	return render(request, "viajes/crear.html", {"form": form})

@login_required
def mis_viajes(request):
	if request.method == "GET":
		conductor = Conductor.objects.get(user_id=request.user.id)
		viajes_creados = Viaje.objects.filter(conductor_id=conductor)
		viajes_solicitados = UsuarioPeticion.objects.filter(user_id=request.user)
	return render(request, "viajes/mis_viajes.html", {'viajes_solicitados': viajes_solicitados, 'viajes_creados': viajes_creados})

@login_required
def mis_viajes_detalle(request, id):
	if request.method == "GET":
		viaje = Viaje.objects.get(id=id)
		lista_usuario_peticion = UsuarioPeticion.objects.filter(viaje_id=id)
		print(lista_usuario_peticion)
	
	return render(request, "viajes/mis_viajes_detalle.html", {'viaje': viaje, 'lista_usuario_peticion': lista_usuario_peticion})

def mis_viajes_detalle_user(request, id, id2):
	usuario = UsuarioPeticion.objects.get(user_id=id2)
	if request.method == "GET":
		usuario = UsuarioPeticion.objects.get(user_id=id2)
	else:
		form = EditarUsuarioPeticionFormulario(request.POST, request.FILES)
		if form.is_valid():
			cd = form.cleaned_data
			print(cd)
			print('ENTRO')
			usuario.__dict__.update(esta_aceptado=cd['esta_aceptado'])
			usuario.save()
		return HttpResponseRedirect("/viajes/misviajes/" + str(id))

	return render(request, "viajes/mis_viajes_detalle_user.html", {'usuario': usuario})
		


# API
def obtener_viaje(request, id):
	viaje = Viaje.objects.get(id=id)
	return JsonResponse({"conductor_nombre": viaje.conductor.username,"conductor": viaje.conductor.id, "descripcion": viaje.descripcion, "fecha": viaje.fecha, "hora": viaje.hora,"capacidad": viaje.capacidad, "imagen_vehiculo": str(viaje.imagen_vehiculo)})

def obtener_viajes(request):
	viajes = Viaje.objects.all().values('id', 'conductor', 'datetime', 'descripcion', 'capacidad', 'ocupados', 'ciudad_destino_id', 'ciudad_origen_id', 'conductor_id', 'imagen_vehiculo')
	viajes = list(viajes)
	return JsonResponse(viajes, safe=False)