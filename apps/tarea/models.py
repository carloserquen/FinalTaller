from django.db import models

class Tarea(models.Model):
    tarea_nombre=models.CharField(max_length=120) 
    tarea_descripcion=models.TextField()
    tarea_data_inicio=models.DateField(auto_now_add=True)
    concluido=models.BooleanField(verbose_name='Concluido', default=False)
    #proyecto = models.ForeignKey(proyecto, related_name='tareas')
    
    def __str__(self):                              
        return self.tarea_nombre


