from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    marca = models.CharField(max_length=50)
    fecha_adquisicion = models.DateField()  

    def __str__(self):
        return self.nombre


