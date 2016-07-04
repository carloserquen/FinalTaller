from django.conf.urls import include, url
from .views import PanelTV
from .views import LoginTV
from .views import RegisterTV
from .views import logout_view
from .views import LoginFormView
from .views import RegisterFormView

from .api import usuarios_get

urlpatterns = [
    url(r'^users/panel/$', PanelTV.as_view(), name='users_panel'),
    url(r'^$', LoginTV.as_view(), name='users_login'),
    url(r'^login/post/$', LoginFormView.as_view(), name='users_login_post'),
    url(r'^users/registro/$', RegisterTV.as_view(), name='users_register'),
    url(r'^users/registro/post/$', RegisterFormView.as_view(), name='users_register_post'),
    url(r'^users/logout/$', logout_view, name='users_logout'),
    #url (r'^tarea/(?P<pk>[0-9]+)/$', views.tarea_detail, name='tarea_detalle'),
    #url(r'^tarea/new/$', views.tarea_new, name='tarea_new'),
    url(r'^api/users/members/$', usuarios_get, name='users_api'),
]