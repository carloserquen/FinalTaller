from django.db import models
from apps.proyectos.models import Proyecto

class Tarea(models.Model):
    nombre = models.CharField(max_length=120) 
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(auto_now_add=True)
    concluido = models.BooleanField(verbose_name='Concluido?', default=False)
    en_desarrollo = models.BooleanField(verbose_name='En desarrollo?', default=False)
    proyecto = models.ForeignKey(Proyecto)
    
    def __str__(self):                              
        return self.nombre
