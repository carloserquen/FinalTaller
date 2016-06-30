from django.contrib import admin
from .models import Proyecto

class ProyectoAdmin(admin.ModelAdmin):
    model = Proyecto
    #list_display = ['nombre','fecha_inicio','concluido']
admin.site.register(Proyecto, ProyectoAdmin)