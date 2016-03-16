from django.conf import settings
from django.conf.urls import include, url, patterns
from .views import *

urlpatterns = [

	url(r'^repUsu/$', 'exa34.apps.Usuario.views.reporteUsuario', name='reporteUsuario'),

    url(r'^formUsu/$', 'exa34.apps.Usuario.views.formUsuario', name='formUsuario'),
    url(r'^formEmp/$', 'exa34.apps.Usuario.views.formEmpresa', name='formEmpresa'),
    url(r'^formCli/$', 'exa34.apps.Usuario.views.formCliente', name='formCliente'),

]
