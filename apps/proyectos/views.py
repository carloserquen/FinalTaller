
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.utils.encoding import force_text
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from .models import Proyecto

from .forms import ProyectoForm

from apps.usuarios.models import Usuario


class ProjectsFV(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy('proyecto_listar')
    template_name = 'proyectos/project_create.html'

    def get_success_url(self):
        """
        Returns the supplied success URL.
        """
        if self.success_url:
            # Forcing possible reverse_lazy evaluation
            url = force_text(self.success_url)
        else:
            raise ImproperlyConfigured(
                "No URL to redirect to. Provide a success_url.")
        return url

    def form_valid(self, form):
        try:
            proyecto = form.save(commit=False)
            proyecto.scrum_master = Usuario.objects.get(user=self.request.user)
            proyecto.save()
        except Exception, e:
            print e, "<-- error --"
        return HttpResponseRedirect(self.get_success_url())


class ProjectsUV(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyectos/proyecto_edit.html"
    success_url = reverse_lazy('proyecto_listar')
    


class ProjectsLV(ListView):
    model = Proyecto
    context_object_name = 'proyectos'
    template_name = 'proyectos/project_list.html'

    def get_queryset(self):
        queryset = Proyecto.objects.filter(scrum_master=Usuario.objects.get(user=self.request.user))
        return queryset


class ProjectDeleteView(DeleteView):
    model = Proyecto
    template_name = "proyectos/project_delete.html"
    success_url = reverse_lazy('proyecto_listar')