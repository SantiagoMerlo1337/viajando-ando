from django.shortcuts import render, HttpResponseRedirect
from .forms import FormularioViajes, NewUserForm
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

# def viajes(request):
	
# 	return 	render(request, 'viajes.html', {})

def viajes(request):
    if request.method == "GET":
        form = FormularioViajes(request.GET)

        if form.is_valid():
            print("los datos finales son:", form.cleaned_data)
            return HttpResponseRedirect("/viajes/")
    else:
        form = FormularioViajes()

    return render(request, "viajes.html", {"form": form})