from django.conf.urls import include, url
from .views import TareasTV
from .views import TareaNuevaTV
from .views import TareaNuevaFormView
from .views import TareaEditTV
from .views import TareaEditarFormView
#from .views import ProjectDeleteView
#from .views import ProjectsFV
#from .views import ProjectsUV

urlpatterns = [
    #url(r'^proyecto/listar/$', ProjectsLV.as_view(), name='proyecto_listar'),
    url(r'^proyecto/(?P<proyecto_pk>\d+)/tareas/$', TareasTV.as_view(), name='proyecto_tareas_panel'),
    url(r'^proyecto/(?P<proyecto_pk>\d+)/tarea/nueva/$', TareaNuevaTV.as_view(), name='tarea_nueva'),
    url(r'^proyecto/tarea/nueva/post/$', TareaNuevaFormView.as_view(), name='tarea_nueva_post'),
    url(r'^proyecto/tarea/(?P<tarea_pk>\d+)/editar/$', TareaEditTV.as_view(), name='tarea_editar'),
    url(r'^proyecto/tarea/(?P<tarea_pk>\d+)/editar/post/$', TareaEditarFormView.as_view(), name='tarea_editar_post'),
    #url(r'^proyecto/nuevo/$', ProjectsFV.as_view(), name='proyecto_nuevo'),
    #url(r'^proyecto/eliminar/(?P<pk>\d+)/$', ProjectDeleteView.as_view(), name='proyecto_eliminar'),
]