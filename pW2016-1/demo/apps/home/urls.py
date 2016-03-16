from django.conf.urls import url
#from django.contrib import admin
from .views import  paginator_report, About, buscar, Student_register, Signup, StudentsReport, Report_professor, PerfilReport, Detail_view, Update_view, Delete_view, Register_professor #Instalacion_view, buscar_view, reporteTecnico_view, pagoTecnico_view#, perfil_view
#from django.conf import settings
urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'home/index.html'}, name='login'),
	url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
	url(r'^about$', About.as_view(), name='about_view'),
	url(r'^register/$', Student_register.as_view(), name='register_student_view'),
	url(r'^student_report/$', StudentsReport.as_view(), name='student_report_view'),
	url(r'^perfil_report/$', PerfilReport.as_view(), name='perfil_report_view'),
    url(r'^buscar/$', buscar, name='buscar_view'),
    url(r'^detalle/(?P<slug>[-\w]+)/$', Detail_view.as_view(), name='detail_view'),
    url(r'^update/(?P<slug>[-\w]+)/$', Update_view.as_view(), name='update_view'),
    url(r'^delete/(?P<slug>[-\w]+)/$', Delete_view.as_view(), name='delete_view'),
    url(r'^signup/$', Signup.as_view(), name='signup_view'),
    url(r'^register_professor/$', Register_professor.as_view(), name='register_professor_view'),
    url(r'^report_professor/$', Report_professor.as_view(), name='report_professor_view'),
    url(r'^paginator_report/page/(?P<pagina>.*)/$', paginator_report, name='paginator_report_view'),
    #url(r'^instalacion/$', Instalacion_view, name = 'Instalacion_view'),
    #url(r'^reporte_fecha/$', buscar_view, name="buscar_view"),
    #url(r'^reporte_tecnico/$', reporteTecnico_view, name='reporteTecnico_view'),
    #url(r'^pago_tecnico/$', pagoTecnico_view, name='pagoTecnico_view'),
    #url(r'^perfil/$', perfil_view, name='perfil_view'),
]