
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from .models import Proyecto
from .forms import ProyectoForm

def list_project(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyecto/proyecto.html', {'proyectos': proyectos})

def proyecto_detail(request, pk): 
    proyecto = get_object_or_404(Proyecto, pk=pk) 
    return render(request, 'proyecto/proyecto_detail.html', {'proyecto': proyecto})

def proyecto_new(request):
    #logging.debug(request.POST)
    if request.method=='POST':
        form=ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'proyecto/proyecto_edit.html',{'form':form})    
    else:
        form=ProyectoForm()
        return render(request, 'proyecto/proyecto_edit.html',{'form':form})


class ProjectsFV(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy('proyecto_listar')
    template_name = 'proyecto/project_create.html'


class ProjectsUV(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyecto/proyecto_edit.html"
    success_url = reverse_lazy('proyecto_listar')
    


class ProjectsLV(ListView):
    model = Proyecto
    context_object_name = 'proyectos'
    template_name = 'proyecto/project_list.html'


class ProjectDeleteView(DeleteView):
    model = Proyecto
    template_name = "proyecto/project_delete.html"
    success_url = reverse_lazy('proyecto_listar')