from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.list_project, name='proyecto_lista'),
    url (r'^proyecto/(?P<pk>[0-9]+)/$', views.proyecto_detail, name='proyecto_detalle'),
    url(r'^proyecto/new/$', views.proyecto_new, name='proyecto_new'),
]