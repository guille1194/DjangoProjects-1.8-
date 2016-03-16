from django.conf.urls import url
from .views import wsPersonas

urlpatterns = [
	
	url(r'^ws/personas/$', wsPersonas, name='wsPersonas_view'),
]