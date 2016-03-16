from django.conf.urls import url
#from django.contrib import admin
from .views import  About, Student_register, StudentsReport, PerfilReport #Instalacion_view, buscar_view, reporteTecnico_view, pagoTecnico_view#, perfil_view
#from django.conf import settings
urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'home/index.html'}, name='login'),
	url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
	url(r'^about$', About.as_view(), name='about_view'),
	url(r'^register/$', Student_register.as_view(), name='register_student_view'),
	url(r'^student_report/$', StudentsReport.as_view(), name='student_report_view'),
	url(r'^perfil_report/$', PerfilReport.as_view(), name='perfil_report_view'),
    #url(r'^instalacion/$', Instalacion_view, name = 'Instalacion_view'),
    #url(r'^reporte_fecha/$', buscar_view, name="buscar_view"),
    #url(r'^reporte_tecnico/$', reporteTecnico_view, name='reporteTecnico_view'),
    #url(r'^pago_tecnico/$', pagoTecnico_view, name='pagoTecnico_view'),
    #url(r'^perfil/$', perfil_view, name='perfil_view'),
]