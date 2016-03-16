from django.conf.urls import url
from .views import wsStudent

urlpatterns = [
	
	url(r'^ws/student/$', wsStudent, name='wsStudent_view'),
]