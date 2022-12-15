"""project URL Configuration

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
from ejemplo.views import (index, saludar_a, sumar,
                             buscar, mostrar_familiares,
                            BuscarFamiliar, AltaFamiliar,
                            ActualizarFamiliar, BorrarFamiliar,
                            mostrar_comidas,BuscarComida,
                            AltaComida, ActualizarComida,
                            BorrarComida, mostrar_consolas,
                            BuscarConsola, AltaConsola,
                            ActualizarConsola,BorrarConsola)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar_a/<nombre>', saludar_a),
    path('sumar/<int:a>/<int:b>/', sumar),
    path('buscar/', buscar),
    path('mi-familia/', mostrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('mi-comida/', mostrar_comidas),
    path('mi-comida/buscar_comida', BuscarComida.as_view()),
    path('mi-comida/alta', AltaComida.as_view()),
    path('mi-comida/actualizar/<int:pk>', ActualizarComida.as_view()),
    path('mi-comida/borrar/<int:pk>', BorrarComida.as_view()),
    path('mi-consola/', mostrar_consolas),
    path('mi-consola/buscar', BuscarConsola.as_view()),
    path('mi-consola/alta', AltaConsola.as_view()),
    path('mi-consola/actualizar/<int:pk>', ActualizarConsola.as_view()),
    path('mi-consola/borrar/<int:pk>', BorrarConsola.as_view()),


]
