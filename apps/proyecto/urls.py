from django.conf.urls import include, url
from . import views
from .views import ProjectsLV
from .views import ProjectDeleteView
from .views import ProjectsFV
from .views import ProjectsUV

urlpatterns = [
    url(r'^proyecto/listar/$', ProjectsLV.as_view(), name='proyecto_listar'),
    url(r'^proyecto/(?P<pk>[0-9]+)/$', views.proyecto_detail, name='proyecto_detalle'),
    url(r'^proyecto/update/(?P<pk>[\w-]+)$', ProjectsUV.as_view(), name='proyecto_update'),
    url(r'^proyecto/nuevo/$', ProjectsFV.as_view(), name='proyecto_nuevo'),
    url(r'^proyecto/eliminar/(?P<pk>\d+)/$', ProjectDeleteView.as_view(), name='proyecto_eliminar'),
]