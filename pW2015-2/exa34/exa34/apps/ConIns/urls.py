from django.conf import settings
from django.conf.urls import include, url, patterns
from .views import *

urlpatterns = [
    url(r'^repTecEsp/$', 'exa34.apps.ConIns.views.reporteTecEsp', name='reporteTecEsp'),
    url(r'^repTecGen/$', 'exa34.apps.ConIns.views.reporteTecGen', name='reporteTecGen'),
    url(r'^repInst/$', 'exa34.apps.ConIns.views.reporteInstalacion', name='reportInstalacion'),
    url(r'^repInv/$', 'exa34.apps.ConIns.views.reporteInventario', name='reporteInventario'),

    url(r'^formInvIns/$', 'exa34.apps.ConIns.views.formInvIns', name='formInvIns'),
    url(r'^formCont/$', 'exa34.apps.ConIns.views.formContrato', name='formContrato'),
    url(r'^formInsta/$', 'exa34.apps.ConIns.views.formInstalacion', name='formInstalacion'),
    url(r'^formInven/$', 'exa34.apps.ConIns.views.formInventario', name='formInventario'),
]
