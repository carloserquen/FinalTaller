from .models import Contacto, Tarea
from .forms import TareaForm
from django.shortcuts import render, get_object_or_404,redirect


def post_list(request):
    contacs = Contacto.objects.all()
    return render(request, 'contacto/contacto.html', {'contacs': contacs})

def list_chore(request):
	tareas = Tarea.objects.all()
	return render(request, 'contacto/contacto.html', {'tareas': tareas})

def tarea_detail(request, pk): 
	tarea = get_object_or_404(Tarea, pk=pk) 
	return render(request, 'contacto/tarea_detail.html', {'tarea': tarea})

def tarea_new(request):
    #logging.debug(request.POST)
    if request.method=='POST':
        form=TareaForm(request.POST)
        if form.is_valid():
            tarea=Tarea()
            tarea.tarea_nombre=request.POST.get('tarea_nombre')
            tarea.tarea_data_inicio=request.POST.get('tarea_data_inicio')
            tarea.save()
            return redirect('contacto.views.tarea_detail', pk=Tarea.tarea_id)
    else:
        form=TareaForm()
        return render(request, 'contacto/tarea_edit.html',{'form':form})


