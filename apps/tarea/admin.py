from django.contrib import admin
from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    model=Tarea
    list_display = ['tarea_nombre','tarea_descripcion','tarea_data_inicio','concluido']
    search_fields = ['tarea_name']
    save_on_top = False
admin.site.register(Tarea, TareaAdmin)
