from django.conf.urls import url
from .views import reporte_chofer1_view

urlpatterns = [
	#url(r'^$', Index_view.as_view(), name='index_view'),
	url(r'^chofer1/$', reporte_chofer1_view, name='reporte_chofer1_view'),
	#url(r'^salida/$', salida_chofer1_view, name='salida_chofer1_view'),
]