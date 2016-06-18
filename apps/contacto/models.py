from django.db import models

class Contacto(models.Model):
    SEXO_CHOICES = (
        (u'masculino',u'Masculino'),
        (u'femenino',u'Femenino'),
        ) 
    ESTADO_CIVIL_CHOICES = (
        (u'soltero',u'Soltero'),
        (u'casado',u'Casado'),
        (u'divorciado',u'Divorciado'),
        (u'viudo',u'Viudo'),
        ) 
    #contacto_id=models.AutoField(primary_key=True)
    contacto_name=models.CharField(max_length=45)
    contacto_nacimiento=models.DateField()
    contacto_sexo=models.CharField(max_length=50,choices = SEXO_CHOICES)
    contacto_estado_civil=models.CharField(max_length=50, choices = ESTADO_CIVIL_CHOICES, verbose_name = 'Estado Civil')
    contacto_email=models.CharField(max_length=50)
    contacto_favorito=models.BooleanField(verbose_name='Favorito')

class Tarea(models.Model):
    #tarea_id=models.AutoField(primary_key=True)
    tarea_nombre=models.CharField(max_length=120) 
    tarea_data_inicio=models.DateField(auto_now_add=True)
    concluido=models.BooleanField(verbose_name='Concluido', default=False)
    
    def __str__(self):                              
        return self.tarea_nombre


class Cuenta(models.Model):
    #cuenta_id=models.AutoField(primary_key=True)
    cuenta_name=models.CharField(max_length=50) 
    cuenta_data_vencimiento=models.DateField()
    pago=models.BooleanField(verbose_name='Pago')

        

