from django import forms

from .models import Proyecto


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre', 'fecha_inicio', )
        widgets = {
        	'nombre': forms.DateInput(attrs={'class': 'form-control'}),
        	'fecha_inicio': forms.DateInput(attrs={'class': 'form-control datepicker', 'id': 'datepicker'}),
        	}