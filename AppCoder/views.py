from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario
from AppCoder.forms import ProfesorFormulario
from AppCoder.models import Curso, Profesor

# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrolloweb", camada="19881")
    curso.save()
    documento = f"El curso es: {curso.nombre}, la camada es: {curso.camada}"
    return HttpResponse(documento)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

# def cursoFormulario(request):
#     if request.method == 'POST':
#         curso = Curso (request.POST['curso'],request.POST['camada'])
#         curso.save()
#         return render(request, "AppCoder/inicio.html")    
#     return render(request, "AppCoder/cursoFormulario.html")

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso (nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario= CursoFormulario()
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario}) 

def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario= ProfesorFormulario()
    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario}) 

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:
        # respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadosPorBusqueda.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)