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

from apps.usuarios.models import Usuario
from .models import Tarea
from .forms import TareaForm
from apps.proyectos.models import Proyecto

from braces.views import LoginRequiredMixin


class TareasTV(LoginRequiredMixin, TemplateView):
    template_name = "tareas/task_list_panel.html"
    #login_url = reverse_lazy('users_login')

    def get_context_data(self, **kwargs):
    	proyecto_pk = kwargs.get('proyecto_pk')
        context = super(TareasTV, self).get_context_data(**kwargs)
        try:
            proyecto = Proyecto.objects.get(pk=proyecto_pk)
            tareas_pendientes = proyecto.tarea_set.all().filter(estado="Pendiente")
            tareas_en_desarrollo = proyecto.tarea_set.all().filter(estado="Desarrollo")
            tareas_concluidas = proyecto.tarea_set.all().filter(estado="Concluido")
            context['proyecto'] = proyecto
            context['tareas_pendientes'] = tareas_pendientes
            context['tareas_pendientes_cantidad'] = len(tareas_pendientes)
            context['tareas_concluidas'] = tareas_concluidas
            context['tareas_concluidas_cantidad'] = len(tareas_concluidas)
            context['tareas_en_desarrollo'] = tareas_en_desarrollo
            context['tareas_en_desarrollo_cantidad'] = len(tareas_en_desarrollo)
        except Exception, e:
            print e, "<-- error --"
        return context

class TareaNuevaTV(TemplateView):
    #success_url = reverse_lazy('proyecto_tareas_panel')
    template_name = 'tareas/task_create.html'

    def get_context_data(self, **kwargs):
        proyecto_pk = kwargs.get('proyecto_pk')
        context = super(TareaNuevaTV, self).get_context_data(**kwargs)
        context['proyecto_pk'] = proyecto_pk
        return context


class TareaEditTV(TemplateView):
    #success_url = reverse_lazy('proyecto_tareas_panel')
    template_name = 'tareas/task_edit.html'

    def get_context_data(self, **kwargs):
        proyecto_pk = kwargs.get('proyecto_pk')
        tarea_pk = kwargs.get('tarea_pk')
        tarea = Tarea.objects.get(pk=tarea_pk)
        context = super(TareaEditTV, self).get_context_data(**kwargs)
        context['proyecto_pk'] = tarea.proyecto.id
        context['tarea'] = tarea
        return context


class TareaNuevaFormView(FormView):
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        print request.POST, "<--registro POST Empleo Datos --"
        #print request.FILES, "<--registro files--"

        response_data = {}
        try:
            proyecto_pk = request.POST.get('proyecto_pk')
            proyecto = Proyecto.objects.get(pk=proyecto_pk)
            
            pendiente = request.POST.get('pendiente', None)
            desarrollo = request.POST.get('desarrollo', None)
            concluido = request.POST.get('concluido', None)

            tarea = Tarea()
            tarea.nombre = request.POST.get('nombre')
            tarea.descripcion = request.POST.get('descripcion')
            tarea.fecha_terminar = request.POST.get('fecha_termino')
            tarea.proyecto = proyecto

            try:
                usuario = Usuario.objects.get(user__username=request.POST.get('username'))
                tarea.owner = usuario
            except Exception, e:
                print "No hay usuario"

            if pendiente:
                tarea.estado = "Pendiente"
            elif desarrollo:
                tarea.estado = "Desarrollo"
            elif concluido:
                tarea.estado = "Concluido"

            tarea.save()

            return HttpResponseRedirect('/proyecto/'+proyecto_pk+'/tareas/')

        except Exception, e:
            print e, "<--Error Empleo Datos Puesto--"
            

class TareaEditarFormView(FormView):
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        print request.POST, "<--registro POST Empleo Datos --"
        #print request.FILES, "<--registro files--"

        response_data = {}
        try:
            tarea_pk = kwargs.get('tarea_pk')
            proyecto_pk = request.POST.get('proyecto_pk')
            proyecto = Proyecto.objects.get(pk=proyecto_pk)
            
            pendiente = request.POST.get('pendiente', None)
            desarrollo = request.POST.get('desarrollo', None)
            concluido = request.POST.get('concluido', None)

            tarea = Tarea.objects.get(pk=tarea_pk)
            tarea.nombre = request.POST.get('nombre')
            tarea.descripcion = request.POST.get('descripcion')
            tarea.fecha_terminar = request.POST.get('fecha_termino')
            tarea.proyecto = proyecto

            try:
                usuario = Usuario.objects.get(user__username=request.POST.get('username'))
                tarea.owner = usuario
            except Exception, e:
                print "No hay usuario"

            if pendiente:
                tarea.estado = "Pendiente"
            elif desarrollo:
                tarea.estado = "Desarrollo"
            elif concluido:
                tarea.estado = "Concluido"

            tarea.save()

            return HttpResponseRedirect('/proyecto/'+proyecto_pk+'/tareas/')

        except Exception, e:
            print e, "<--Error Empleo Datos Puesto--"
            

class TareasLV(ListView):
    model = Tarea
    context_object_name = 'tareas'
    template_name = 'tareas/task_list.html'

    def get_queryset(self):
        queryset = Tarea.objects.filter(owner=Usuario.objects.get(user=self.request.user))
        print len(queryset), "<-- len --"
        return queryset

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = "tareas/task_delete.html"
    success_url = reverse_lazy('mis_tareas_listar')        