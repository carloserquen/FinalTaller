from django.conf.urls import include, url
from . import views
from .views import ProjectsLV
from .views import ProjectDeleteView

urlpatterns = [
    url(r'^listar/$', ProjectsLV.as_view(), name='proyecto_listar'),
    url (r'^proyecto/(?P<pk>[0-9]+)/$', views.proyecto_detail, name='proyecto_detalle'),
    url(r'^proyecto/new/$', views.proyecto_new, name='proyecto_new'),
    url(r'^proyecto/eliminar/(?P<pk>\d+)/$', ProjectDeleteView.as_view(), name='proyecto_eliminar'),
]