from django.conf.urls import include, url
from .views import TareasTV
#from .views import ProjectDeleteView
#from .views import ProjectsFV
#from .views import ProjectsUV

urlpatterns = [
    #url(r'^proyecto/listar/$', ProjectsLV.as_view(), name='proyecto_listar'),
    url(r'^proyecto/(?P<proyecto_pk>[\w-]+)/tareas/$', TareasTV.as_view(), name='proyecto_tareas'),
    #url(r'^proyecto/nuevo/$', ProjectsFV.as_view(), name='proyecto_nuevo'),
    #url(r'^proyecto/eliminar/(?P<pk>\d+)/$', ProjectDeleteView.as_view(), name='proyecto_eliminar'),
]