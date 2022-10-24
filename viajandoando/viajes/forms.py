from django import forms
from viajes.models import  Viaje

#WIDGETS

class DatePickerInput(forms.DateInput):
    input_type = 'date'
class TimePickerInput(forms.TimeInput):
    input_type = 'time'

#FORMS

class BuscarViajesFormulario(forms.ModelForm):
	fecha_inicio = forms.DateField(widget=DatePickerInput(attrs={'type': 'date'}))
	fecha_fin = forms.DateField(widget=DatePickerInput(attrs={'type': 'date'}))
	class Meta:
		model = Viaje
		fields = ['ciudad_origen','ciudad_destino',]

class CrearViajeFormulario(forms.ModelForm):
	class Meta:
		model = Viaje
		fields = ['ciudad_origen','ciudad_destino', 'descripcion', 'capacidad', 'fecha', 'hora', 'imagen_vehiculo',]
		widgets = {
			'fecha': DatePickerInput(attrs={'type': 'date'}),
			'hora': TimePickerInput()
		}

class CrearUsuarioPeticionFormulario(forms.Form):
	user = forms.IntegerField()
	viaje = forms.IntegerField()

class EditarUsuarioPeticionFormulario(forms.Form):
	esta_aceptado = forms.BooleanField()