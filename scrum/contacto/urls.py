from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.list_chore),
    url (r'^tarea/(?P<pk>[0-9]+)/$', views.tarea_detail),
    url(r'^tarea/new/$', views.tarea_new, name='tarea_new'),
]