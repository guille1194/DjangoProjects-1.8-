from django.conf.urls import url
#from django.contrib import admin
from .views import Instalacion_view, buscar_view, reporteTecnico_view, pagoTecnico_view#, perfil_view


urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'principal/index.html'}, name='login'),
	url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^instalacion/$', Instalacion_view, name = 'Instalacion_view'),
    url(r'^reporte_fecha/$', buscar_view, name="buscar_view"),
    url(r'^reporte_tecnico/$', reporteTecnico_view, name='reporteTecnico_view'),
    url(r'^pago_tecnico/$', pagoTecnico_view, name='pagoTecnico_view'),
    #url(r'^perfil/$', perfil_view, name='perfil_view'),
]
