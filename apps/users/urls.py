from django.conf.urls import include, url
from .views import PanelTV
from .views import LoginTV
from .views import RegisterTV

urlpatterns = [
    url(r'^users/panel/$', PanelTV.as_view(), name='users_panel'),
    url(r'^$', LoginTV.as_view(), name='users_login'),
    url(r'^registro/$', RegisterTV.as_view(), name='users_register'),
    #url (r'^tarea/(?P<pk>[0-9]+)/$', views.tarea_detail, name='tarea_detalle'),
    #url(r'^tarea/new/$', views.tarea_new, name='tarea_new'),
]