#Esta vista permitirá a los usuarios agregar nuevos equipos.

from django import forms
from .models import Equipo
from django.core.exceptions import ValidationError
from datetime import date

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'descripcion', 'marca', 'fecha_adquisicion']
    

    #creamos las validaciones para el formulario
    #usamos el campo nombre
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError('El nombre del equipo es requerido.')
        return nombre
    
    #usamos el campo fecha
    
    def clean_fecha_adquisicion(self):
        fecha_adquisicion = self.cleaned_data.get('fecha_adquisicion')
        if fecha_adquisicion and fecha_adquisicion > date.today():
            raise ValidationError('La fecha de adquisición no puede ser en el futuro.')
        return fecha_adquisicion
    
    


