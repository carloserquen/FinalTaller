from .models import Tarea
from .forms import TareaForm
from django.shortcuts import render, get_object_or_404,redirect


def list_task(request):
    tareas = Tarea.objects.all()
    return render(request, 'tarea/tarea.html', {'tareas': tareas})

def tarea_detail(request, pk): 
    tarea = get_object_or_404(Tarea, pk=pk) 
    return render(request, 'tarea/tarea_detail.html', {'tarea': tarea})

def tarea_new(request):
    #logging.debug(request.POST)
    if request.method=='POST':
        form=TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'tarea/tarea_edit.html',{'form':form})    
    else:
        form=TareaForm()
        return render(request, 'tarea/tarea_edit.html',{'form':form})


