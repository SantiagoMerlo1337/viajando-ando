"""viajandoando URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import TemplateView
from viajes import views as viajes_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

import viajes

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("register", user_views.register_request, name="register"),
    path("activate/<uidb64>/<token>", user_views.activate, name="activate"),
    path("viajes/", viajes_views.viajes, name="viajes"),
    path("viajes/misviajes", viajes_views.mis_viajes, name="mis viajes"),
    path("viajes/misviajes/<int:id>", viajes_views.mis_viajes_detalle, name="mis_viajes_detalle"),
    path("viajes/crear/", viajes_views.crear_viaje, name="crear viaje"),
    path("accounts/user/<int:id>", user_views.perfil_request, name="perfil"),
    path('api/viajes/<int:id>', viajes_views.obtener_viaje, name="obtener viaje"),
    path('api/viajes', viajes_views.obtener_viajes, name="obtener viajes"),
    path('search/', include('haystack.urls'), name="search"),
    path("robots.txt", user_views.robots_txt),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)