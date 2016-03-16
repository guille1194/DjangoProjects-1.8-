from django.conf.urls import url
from .views import rechazo_chofer1_view, salida_chofer1_view

urlpatterns = [
	#url(r'^$', Index_view.as_view(), name='index_view'),
	url(r'^rechazo/$', rechazo_chofer1_view, name='rechazo_chofer1_view'),
	url(r'^salida/$', salida_chofer1_view, name='salida_chofer1_view'),
]