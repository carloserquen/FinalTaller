from django.db import models
from apps.usuarios.models import Usuario
from apps.proyectos.models import Proyecto

class Tarea(models.Model):
    nombre = models.CharField(max_length=120) 
    descripcion = models.TextField(blank=True, null=True)
    fecha_terminar = models.DateField()

    estado_opciones = [
        ('Pendiente','Pendiente'),
        ('Desarrollo','Desarrollo'),
        ('Concluido','Concluido'),
    ]

    estado = models.CharField(max_length=15,
                                      choices=estado_opciones, blank=True, null=True)
    proyecto = models.ForeignKey(Proyecto)
    owner = models.ForeignKey(Usuario, blank=True, null=True)
    
    def __str__(self):                              
        return self.nombre
