from django.contrib import admin
from .models import Contacto, Tarea, Cuenta

class ContactoAdmin(admin.ModelAdmin):
    model=Contacto
    list_display = ['contacto_name','contacto_email','contacto_estado_civil','contacto_favorito']
    list_filter = ['contacto_sexo','contacto_estado_civil']
    search_fields = ['contacto_name']
    save_on_top = False
admin.site.register(Contacto, ContactoAdmin)

class TareaAdmin(admin.ModelAdmin):
	model = Tarea
	list_display = ['tarea_nombre','tarea_data_inicio','concluido']
	search_fields = ['tarea_nombre']
	save_on_top = False
admin.site.register(Tarea,TareaAdmin)

class CuentaAdmin(admin.ModelAdmin):
	model = Tarea
	list_display = ['cuenta_name','cuenta_data_vencimiento','pago']
	search_fields = ['tarea_name']
	#save_on_top = False
admin.site.register(Cuenta,CuentaAdmin)