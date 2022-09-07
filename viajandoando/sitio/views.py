from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect
from sitio.models import Viaje
from .forms import FormularioCreacionViaje, FormularioViajes, NewUserForm
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registración realizada." )
			return redirect("/")
		messages.error(request, "No se pudo registrar. Información no válida.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

@login_required
def mis_viajes(request):	
	return render(request, 'mis_viajes.html', {},)

def home(request):
    return render(request, 'base.html', {})

#VER VIAJES
def viajes(request):
	if request.method == "GET":
		form = FormularioViajes(request.GET)
		viajes = ''
		if form.is_valid() and form.cleaned_data['fecha_inicio'] < form.cleaned_data['fecha_fin'] and form.cleaned_data['ciudad_origen'] != form.cleaned_data['ciudad_destino']:
			date1 = form.cleaned_data['fecha_inicio']
			date2 = form.cleaned_data['fecha_fin']
			origen = form.cleaned_data['ciudad_origen']
			destino = form.cleaned_data['ciudad_destino']
			viajes = Viaje.objects.filter(datetime__range=[date1, date2], ciudad_origen=origen, ciudad_destino=destino)
		else:
			form = FormularioViajes()
	return render(request, "viajes.html", {"form": form, 'lista_viajes': viajes})

@login_required
def creacion_viaje(request):
	form = FormularioCreacionViaje(request.POST)
	if form.is_valid() and form.cleaned_data['fecha'] > date.today() and form.cleaned_data['ciudad_origen'] != form.cleaned_data['ciudad_destino']:
		viaje = form.save(commit=False)
		viaje.datetime = datetime.combine(viaje.fecha, viaje.hora)
		viaje.conductor = request.user
		form.save()
		return HttpResponseRedirect("/viajes/")
	else:
		form = FormularioCreacionViaje()
	return render(request, "creacion_viaje.html", {"form": form})

#return render(request, "crear_viaje.html", {"form": form})
