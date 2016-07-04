from django import forms

from .models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ('nombre', 'descripcion', 'fecha_terminar', )
        widgets = {
        	'nombre': forms.DateInput(attrs={'class': 'form-control'}),
        	'fecha_terminar': forms.DateInput(attrs={'class': 'form-control datepicker', 'id': 'datepicker'}),
        	}