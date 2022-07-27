
from contextvars import Context
import datetime
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context, loader
from httplib2 import Http
from AppCoder.models import Curso, Familiar

def saludo(request):
    return HttpResponse("hola mundo")

def mi_nombre(request, nombre):
    return HttpResponse(f"Hola {nombre}")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es el día: {dia}"
    return HttpResponse(documentoDeTexto)

def probando_template(request):
    miHtml = open(r"C:\Users\gjdba\Documents\CoderHouse\coder40150\desafio_entregable_clase_18\desafio_clase_18\desafio_clase_18\plantillas\template1.html","r")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def notas(request):
    datos = { "notas": [9, 4, 3, 7, 10, 8, 5, 10], "estudiante": "Gaston" }
    archivo = open(r"C:\Users\gjdba\Documents\CoderHouse\coder40150\desafio_entregable_clase_18\desafio_clase_18\desafio_clase_18\plantillas\template2.html", "r")
    contenido = archivo.read()
    archivo.close()
    plantilla = Template(contenido)
    contexto = Context(datos)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def notas_loader(request):
    datos = { "notas": [9, 4, 3, 7, 10, 8, 5, 10], "estudiante": "Gaston" }
    plantilla = loader.get_template("template3.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def guardar_curso(request):
    curso = Curso(nombre = "Desarrollo Web", camada="19881")
    curso.save()
    documentoDeTexto = f"---> Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)

def guarda_muestra_datos(request):
    if 'id_borrar' in request.GET:
        try:
            Familiar.objects.filter(id=int(request.GET['id_borrar'])).delete()
        except Exception as e:
            print(f"Error al intentar borrar {e}")
    # Tuve que investigar un poco cómo obtener los datos de la base de datos porque hasta la clase 18 no vi que enseñaran cómo..
    tabla_sql = Familiar.objects.all()
    # Esto para tener una lista iterable en python de la consulta a la DB
    result = Familiar.objects.values()
    list_result = [entry for entry in result]
    print(f"imprimiendo list_result {list_result} tipo {type(list_result)} largo {len(list_result)}") # un poco de impresion para entender la estructura
    existe=False
    existe_registro = ""
    # Un poco de validación de datos
    #if len(str(request.GET['dni'])) >= 1:
    for x in range(len(list_result)):
        try:
            if list_result[x]["dni"] == int(request.GET['dni']): existe=True
        except Exception as e:
            print(f"Error {e} No se obtuvo un GET aún.")
    if 'fname' in request.GET:
        if len(str(request.GET['dni'])) >= 8 and not existe: #esto es re cabeza jaja
            _nombre = request.GET['fname']
            _dni = request.GET['dni']
            _fnac = request.GET['fec_nac']
            _familiar = Familiar(nombre_apellido = _nombre, dni = _dni, fecha_nacimiento = _fnac)
            _familiar.save()
        elif existe:
            print("Ya existe ese registro")
            existe_registro = "Ya existe el registro (dni), intente con otro"

    datos = {"tabla_sql":tabla_sql, "ya_existe_el_registro":existe_registro}
    plantilla = loader.get_template("template4.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

