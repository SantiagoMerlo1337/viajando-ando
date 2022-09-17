from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect
from sitio.models import Viaje, Conductor, UsuarioPeticion
from .forms import FormularioCreacionViaje, FormularioViajes, NewUserForm
from django.shortcuts import  render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date


from django.contrib.auth import login, get_user_model

from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .decorators import user_not_authenticated

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('home')

def activateEmail(request, user, to_email):
    mail_subject = "Activa tu cuenta de ViajandoAndo."
    message = render_to_string("users/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Estimado <b>{user}</b>, ingresa en tu mail <b>{to_email}</b> y verifica la bandeja de entrada el mail de confirmacion para confirmar la registracion de su cuenta. \
		<b>Nota:</b> Revisa en la seccion de spam')
    else:
        messages.error(request, f'Hubo un problema enviando el mail a <b>{to_email}</b>, revisa si lo has escrito correctamente.')

@user_not_authenticated
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			activateEmail(request, user, form.cleaned_data.get('email'))
			return redirect("home")
		else:
			for error in list(form.errors.values()):
				messages.error(request, error)
		
	else:
		form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

@login_required
def mis_viajes(request):	
	return render(request, 'mis_viajes.html', {},)

def home(request):
    return render(request, 'base.html', {})

def viajes(request):
	form = ''
	viajes = ''
	origen = ''
	destino = ''
	if request.method == "GET":
		form = FormularioViajes(request.GET)
		if form.is_valid() and form.cleaned_data['fecha_inicio'] < form.cleaned_data['fecha_fin'] and form.cleaned_data['ciudad_origen'] != form.cleaned_data['ciudad_destino']:
			date1 = form.cleaned_data['fecha_inicio']
			date2 = form.cleaned_data['fecha_fin']
			origen = form.cleaned_data['ciudad_origen']
			destino = form.cleaned_data['ciudad_destino']
			viajes = Viaje.objects.filter(datetime__range=[date1, date2], ciudad_origen=origen, ciudad_destino=destino)
	return render(request, "viajes.html", {"form": form, 'lista_viajes': viajes, 'origen':origen, 'destino': destino})

@login_required
def creacion_viaje(request):
	form = FormularioCreacionViaje(request.POST, request.FILES)
	prueba = False
	if Conductor.objects.filter(user=request.user).count() == 1:
		prueba = True
		
	if form.is_valid() and form.cleaned_data['fecha'] > date.today() and form.cleaned_data['ciudad_origen'] != form.cleaned_data['ciudad_destino'] and prueba == True:
		viaje = form.save(commit=False)
		viaje.datetime = datetime.combine(viaje.fecha, viaje.hora)
		viaje.conductor = request.user
		form.save()
		return HttpResponseRedirect("/viajes/")
	else:
		form = FormularioCreacionViaje()
	return render(request, "creacion_viaje.html", {"form": form})