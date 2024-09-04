#definimos las funciones de agregar, eliminar y obtener la lista de los equipos

from .models import Equipo


def obtener_lista_equipos():
    """Devuelve una lista de todos los equipos."""
    return Equipo.objects.all()

def agregar_equipo(datos_equipo):
    """Agrega un nuevo equipo a la base de datos."""
    equipo = Equipo(
        nombre=datos_equipo.get('nombre'),
        descripcion=datos_equipo.get('descripcion'),
        marca=datos_equipo.get('marca'),
        fecha_adquisicion=datos_equipo.get('fecha_adquisicion')
    )
    equipo.save()
    return equipo

def eliminar_equipo(equipo_id):
    """Elimina un equipo dado su ID."""
    equipo = Equipo.objects.get(id=equipo_id)
    equipo.delete()
