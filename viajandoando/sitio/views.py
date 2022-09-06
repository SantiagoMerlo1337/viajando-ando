from subprocess import CREATE_NEW_CONSOLE
from django.shortcuts import render, HttpResponseRedirect

from sitio.models import Viaje, Ciudad, Provincia, User
from .forms import FormularioCreacionViaje, FormularioViajes, NewUserForm
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

def viajes(request):
	if request.method == "GET":
		form = FormularioViajes(request.GET)
		if form.is_valid():
			return HttpResponseRedirect("/viajes/")
		else:
			form = FormularioViajes()
		viajes = Viaje.objects.all()
	return render(request, "viajes.html", {"form": form, 'lista_viajes':viajes})

@login_required
def creacion_viaje(request):
	if request.method == "GET":
		form = FormularioCreacionViaje(request.GET)
		if form.is_valid():
			return HttpResponseRedirect("/viajes/")
		else:
			form = FormularioCreacionViaje()
	return render(request, "creacion_viaje.html", {"form": form})

#return render(request, "crear_viaje.html", {"form": form})

# def crear_viaje(request):
# 	if request.method == "POST":
# 		form = FormularioCreacionViaje(request.GET)
# 		if form.is_valid() and form.Meta.fields[0] != form.Meta.fields[1] :

# 			return HttpResponseRedirect("/viajes/")
# 		else:
# 			form = FormularioCreacionViaje()
# 	return render(request, "creacion_viaje.html", {"form": form})