from django.shortcuts import render

from django.shortcuts import render, HttpResponseRedirect
from sitio.models import *
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def viajes(request):
    return render(request, 'viajes.html', {},)

def home(request):
    return render(request, 'base.html', {})


# def registrarse(request):

#     usuario = Usuario()

#     if request.method == "POST":
#         form = Form_Registro_Usuario(request.POST)

#         if form.is_valid():
#             nuevoUsuario = Usuario()
#             nuevoUsuario.Username = form.cleaned_data['Username']
#             nuevoUsuario.Email = form.cleaned_data['Email']
#             nuevoUsuario.Password = form.cleaned_data['Password']
#             nuevoUsuario.ConfirmPassword = form.cleaned_data['ConfirmPassword']
#             nuevoUsuario.save()
#             print("se guardo")
#             return HttpResponseRedirect("")
#         else:
#             form = Form_Registro_Usuario()

#     else:
#         form = Form_Registro_Usuario()
    

#     return render(request, "registrarse.html", {"form": form})