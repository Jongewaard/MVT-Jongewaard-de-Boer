"""desafio_clase_18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from desafio_clase_18.view import saludo, dia_de_hoy, mi_nombre, probando_template, notas, notas_loader, guardar_curso, guarda_muestra_datos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', guarda_muestra_datos), #para que abra de una la pág del desafío entregable
    path('saludo/', saludo), #mi primer impresión
    path('dia_de_hoy/', dia_de_hoy), #mi primer pasaje de parámetros
    path('mi_nombre/<nombre>/', mi_nombre), #mi primer toma de datos externos
    path('probando_template/', probando_template), #mi primer template
    path('notas/', notas), #mi primer template con datos
    path('notas_loader/', notas_loader), #mi primer template y loader
    path('guardar_curso/', guardar_curso), #mi primer guardada de datos a la db
    path('guarda_muestra_datos/', guarda_muestra_datos), #guardando y mostrando datos

]
