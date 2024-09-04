#agrega las rutas para las vistas:

from django.urls import path
from .views import agregar_equipo_view, lista_equipos_view, detalle_equipo_view, eliminar_equipo_view

urlpatterns = [
    path('', lista_equipos_view, name='lista_equipos'),  # Ruta para la lista de equipos
    path('agregar/', agregar_equipo_view, name='agregar_equipo'),  # Ruta para el formulario de creación de equipos
    path('<int:pk>/', detalle_equipo_view, name='detalle_equipo'),  # Ruta para ver detalles de un equipo específico
    path('eliminar/<int:pk>/', eliminar_equipo_view, name='eliminar_equipo'),  # Ruta para eliminar un equipo
]

