from django.conf.urls import include, url
from .views import PanelTV

urlpatterns = [
    url(r'^panel/$', PanelTV.as_view(), name='users_panel'),
    #url (r'^tarea/(?P<pk>[0-9]+)/$', views.tarea_detail, name='tarea_detalle'),
    #url(r'^tarea/new/$', views.tarea_new, name='tarea_new'),
]