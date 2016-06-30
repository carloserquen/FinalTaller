from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.utils.encoding import force_text
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from .models import Tarea
from apps.proyectos.models import Proyecto

from braces.views import LoginRequiredMixin


class TareasTV(LoginRequiredMixin, TemplateView):
    template_name = "tareas/task_list.html"
    #login_url = reverse_lazy('users_login')

    def get_context_data(self, **kwargs):
    	proyecto_pk = kwargs.get('proyecto_pk')
        context = super(TareasTV, self).get_context_data(**kwargs)
        proyecto = Proyecto.objects.get(pk=proyecto_pk)
        tareas_pendientes = proyecto.tarea_set.all().filter(concluido=False, en_desarrollo=False)
        tareas_en_desarrollo = proyecto.tarea_set.all().filter(en_desarrollo=True)
        tareas_concluidas = proyecto.tarea_set.all().filter(concluido=True)
        context['proyecto'] = proyecto
        context['tareas_pendientes'] = tareas_pendientes
        context['tareas_pendientes_cantidad'] = len(tareas_pendientes)
        context['tareas_concluidas'] = tareas_concluidas
        context['tareas_concluidas_cantidad'] = len(tareas_concluidas)
        context['tareas_en_desarrollo'] = tareas_en_desarrollo
        context['tareas_en_desarrollo_cantidad'] = len(tareas_en_desarrollo)
        return context