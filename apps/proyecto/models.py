from django.db import models

class Proyecto(models.Model):
    proyecto_nombre=models.CharField(max_length=120) 
    proyecto_data_inicio=models.DateField(auto_now_add=True)
    concluido=models.BooleanField(verbose_name='Concluido', default=False)
    
    def __str__(self):                              
        return self.proyecto_nombre


