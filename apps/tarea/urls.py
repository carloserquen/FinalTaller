from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.list_task, name='tarea_lista'),
    url (r'^tarea/(?P<pk>[0-9]+)/$', views.tarea_detail, name='tarea_detalle'),
    url(r'^tarea/new/$', views.tarea_new, name='tarea_new'),
]