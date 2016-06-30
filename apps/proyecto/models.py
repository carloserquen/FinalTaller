from django.db import models

class Proyecto(models.Model):
    nombre=models.CharField(max_length=120) 
    fecha_inicio=models.DateField()
    concluido=models.BooleanField(verbose_name='Concluido?', default=False)
    
    def __str__(self):                              
        return self.nombre


