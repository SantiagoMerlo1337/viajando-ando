from django.shortcuts import render
from django.shortcuts import  render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

from viajes.views import viajes
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .decorators import user_not_authenticated
from viajes.models import *
from users.models import *
from .forms import *

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

        messages.success(request, "Gracias por la confirmacion de tu correo. Ahora puedes acceder con tu cuenta.")
        return redirect('login')
    else:
        messages.error(request, "Link de activacion invalido!")

    return redirect('home')

def activateEmail(request, user, to_email):
    mail_subject = "Activa tu cuenta de ViajandoAndo."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Estimado {user}, ingresa en tu mail {to_email} y verifica la bandeja de entrada el mail de confirmacion para confirmar la registracion de su cuenta. Nota: Revisa en la seccion de spam')
    else:
        messages.error(request, f'Hubo un problema enviando el mail a {to_email}, revisa si lo has escrito correctamente.')

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

def perfil_request(request, id):
    if request.method == "GET":
        usuario = User.objects.get(pk=id)
        usuario_viajes = Viaje.objects.filter(conductor=usuario.id).count()
        try:
            conductor = Conductor.objects.get(user_id=usuario.id)
            return render (request, "perfil.html", {"usuario": usuario, "usuario_viajes": usuario_viajes, "conductor": conductor})
        except:
            print('error')
            return render (request, "perfil.html", {"usuario": usuario, "usuario_viajes": usuario_viajes})
        
        