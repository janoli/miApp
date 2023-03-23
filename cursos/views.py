from django.shortcuts import render
from .models import Curso

# Create your views here.
from django.http import HttpResponse


def index(request):
    cursos = Curso.objects.all()
    return render(request, 'index.html', {'cursos': cursos})


def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {'cursos': cursos})

