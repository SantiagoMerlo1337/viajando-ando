from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sitio.models import Viaje

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

#WIDGET
class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'
class TimePickerInput(forms.TimeInput):
    input_type = 'time'


class FormularioViajes(forms.ModelForm):
	fecha_inicio = forms.DateTimeField(widget=DateTimePickerInput(attrs={'type': 'date'}))
	fecha_fin = forms.DateTimeField(widget=DateTimePickerInput(attrs={'type': 'date'}))
	class Meta:
		model = Viaje
		fields = ['ciudad_origen','ciudad_destino',]

class FormularioCreacionViaje(forms.ModelForm):
	class Meta:
		model = Viaje
		fields = ['ciudad_origen','ciudad_destino', 'descripcion', 'capacidad', 'fecha', 'hora', 'imagen',]
		widgets = {
			'fecha': DateTimePickerInput(attrs={'type': 'date'}),
			'hora': TimePickerInput()
		}
		
class Viaje_Id(forms.Form):
	viaje_id = forms.IntegerField()