from django.shortcuts import render, HttpResponseRedirect
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
		if form.is_valid() and form.cleaned_data['fecha_inicio'] < form.cleaned_data['fecha_fin'] and form.cleaned_data['ciudad_origen'] != form.cleaned_data['ciudad_destino']:\
			
			date1 = form.cleaned_data['fecha_inicio']
			date2 = form.cleaned_data['fecha_fin']
			origen = form.cleaned_data['ciudad_origen']
			destino = form.cleaned_data['ciudad_destino']
			viajes = Viaje.objects.filter(datetime__range=[date1, date2], ciudad_origen=origen, ciudad_destino=destino)
	else:
		if request.user.is_authenticated:
			form = CrearUsuarioPeticionFormulario(request.POST, request.FILES)
			if form.is_valid():
				cd = form.cleaned_data
				viaje = Viaje.objects.get(pk=cd['viaje'])
				pc = UsuarioPeticion(
					viaje = viaje,
					user = request.user
				)
				if UsuarioPeticion.objects.filter(user=request.user, viaje=viaje).count() == 0 and viaje.conductor.user != request.user:
					pc.save()
				else:
					messages.error(request, 'Error en la solicitud')
				return HttpResponseRedirect("/viajes")
		else:
			return HttpResponseRedirect("/viajes", messages.error(request, f'Debe iniciar sesión para solicitar unirse a un viaje'))
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
		viaje.disponible = viaje.capacidad
		form.save()
		return HttpResponseRedirect("/viajes", messages.error(request, f'El viaje ha sido creado con éxito.'))
	else:
		form = CrearViajeFormulario()
	return render(request, "viajes/crear.html", {"form": form})

@login_required
def mis_viajes(request):
	viajes_creados = ''
	if request.method == "GET":
		try:
			conductor = Conductor.objects.get(user_id=request.user.id)
			viajes_creados = Viaje.objects.filter(conductor_id=conductor)
		except:
			print('No es conductor.')
		viajes_solicitados = UsuarioPeticion.objects.filter(user_id=request.user)
	return render(request, "viajes/mis_viajes.html", {'viajes_solicitados': viajes_solicitados, 'viajes_creados': viajes_creados})

@login_required
def mis_viajes_detalle(request, id):
	viaje = Viaje.objects.get(id=id)
	print(id)
	if request.user == viaje.conductor.user:
		lista_usuario_peticion = UsuarioPeticion.objects.filter(viaje_id=id)
		if request.method == "POST":
			id_peticion = request.POST["esta_aceptado"]
			peticion = UsuarioPeticion.objects.get(pk=id_peticion)
			if 'aceptar' in request.POST:
				if peticion.viaje.disponible > 0 and (peticion.esta_aceptado == None or peticion.esta_aceptado == False):
					peticion.viaje.disponible = peticion.viaje.disponible - 1
				peticion.esta_aceptado = True
				peticion.viaje.save()
				peticion.save()
			else:
				if peticion.esta_aceptado == True:
					peticion.viaje.disponible = peticion.viaje.disponible + 1
				peticion.esta_aceptado = False
				peticion.viaje.save()
				peticion.save()
			return HttpResponseRedirect("/viajes/misviajes")
	return render(request, "viajes/mis_viajes_detalle.html", {'viaje': viaje, 'lista_usuario_peticion': lista_usuario_peticion})

	
# API
def obtener_viaje(request, id):
	viaje = Viaje.objects.get(id=id)
	return JsonResponse({"conductor_nombre": viaje.conductor.username,"conductor": viaje.conductor.id, "descripcion": viaje.descripcion, "fecha": viaje.fecha, "hora": viaje.hora,"capacidad": viaje.capacidad, "imagen_vehiculo": str(viaje.imagen_vehiculo)})

def obtener_viajes(request):
	viajes = Viaje.objects.all().values('id', 'conductor', 'datetime', 'descripcion', 'capacidad', 'ocupados', 'ciudad_destino_id', 'ciudad_origen_id', 'conductor_id', 'imagen_vehiculo')
	viajes = list(viajes)
	return JsonResponse(viajes, safe=False)