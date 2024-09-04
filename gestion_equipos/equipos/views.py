#Esta vista mostrará todos los equipos almacenados en la base de datos.

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .services import obtener_lista_equipos
from .services import agregar_equipo
from .services import eliminar_equipo
from .models import Equipo
from .forms import EquipoForm


def agregar_equipo_view(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            agregar_equipo(datos)
            return redirect('lista_equipos')
    else:
        form = EquipoForm()
    return render(request, 'equipos/agregar_equipo.html', {'form': form})

def lista_equipos_view(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/lista_equipos.html', {'equipos': equipos})

def detalle_equipo_view(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    return render(request, 'equipos/detalle_equipo.html', {'equipo': equipo})

def eliminar_equipo_view(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == "POST":
        equipo.delete()
        return redirect('lista_equipos')
    return render(request, 'equipos/eliminar_equipo.html', {'equipo': equipo})






