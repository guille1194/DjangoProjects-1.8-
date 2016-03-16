from django.conf import settings
from django.conf.urls import include, url, patterns
from .views import *

urlpatterns = [
	url(r'^index/$', 'exa34.apps.General.views.index', name='index'),
	url(r'^$', 'django.contrib.auth.views.login', {'template_name' : 'General/login.html'} , name='login'),
	url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
]
