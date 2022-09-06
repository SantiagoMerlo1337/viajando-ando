from dataclasses import field
from datetime import datetime
from email.message import EmailMessage
from tkinter import Widget
from tokenize import blank_re
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sitio.models import *
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime, AdminTimeWidget


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'


class FormularioViajes(forms.ModelForm):
	fecha_inicio = forms.DateTimeField(widget=DateTimePickerInput(attrs={'type': 'date'}))
	fecha_fin = forms.DateTimeField(widget=DateTimePickerInput(attrs={'type': 'date'}))
	class Meta:
		model = Viaje
		fields = ['ciudad_origen','ciudad_destino',]

class FormularioCreacionViaje(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['ciudad_origen','ciudad_destino', 'descripcion', 'capacidad', 'fecha',]
		
