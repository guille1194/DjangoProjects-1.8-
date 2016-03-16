from django.conf.urls import url
#from django.contrib import admin
from .views import Inventarios_view, ventas_view, populares_view, reporte_ventas_periodo_view, reporte_ventas_dia_view, consulta_view


urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'principal/index.html'}, name='login'),
	url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^inventarios/$', Inventarios_view.as_view(), name = 'inventarios_view'),
    url(r'^ventas/$', ventas_view, name="ventas_view"),
    url(r'^populares/$', populares_view, name="populares_view"),
    url(r'^reporte_ventas_periodo/$', reporte_ventas_periodo_view, name='reporte_ventas_periodo_view'),
    url(r'^reporte_ventas_dia/$', reporte_ventas_dia_view, name='reporte_ventas_dia_view'),
    url(r'^consultar/$', consulta_view, name='consulta_view'),
    # #url(r'^perfil/$', perfil_view, name='perfil_view'),
]
