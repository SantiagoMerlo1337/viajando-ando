from django.shortcuts import render

from django.shortcuts import render, HttpResponseRedirect
from .forms import NewUserForm
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def viajes(request):
    return render(request, 'viajes.html', {},)

def home(request):
    return render(request, 'base.html', {})