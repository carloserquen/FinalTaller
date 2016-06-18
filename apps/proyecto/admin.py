from django.contrib import admin
from .models import Proyecto

class ProyectoAdmin(admin.ModelAdmin):
    model=Proyecto
    list_display = ['proyecto_nombre','proyecto_data_inicio','concluido']
    search_fields = ['proyecto_name']
    save_on_top = False
admin.site.register(Proyecto, ProyectoAdmin)
