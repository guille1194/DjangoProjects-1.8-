from django.conf.urls import url
from .views import About_view, DatosFormSet, NomeCreen_view, reporte, buscar, editar, detail_view, Signup, Reporte2, Detail_report, Reporte3
urlpatterns = [
	
	#url(r'^$', Index_view.as_view(), name='index_view'),
	url(r'^$', 'django.contrib.auth.views.login', {'template_name':'home/index_view.html'}, name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
	url(r'^signup/$', Signup.as_view(), name='signup_view'),
	url(r'^about/$', About_view.as_view(), name='about_view'),
	#url(r'^dato/$', DatosSet.as_view(), name='datos_view'),
	url(r'^dato/$', DatosFormSet.as_view(), name='datos_view'),
	#url(r'^dato/$', Datos_register.as_view(), name='datos_view'),
	url(r'^nomecreen/$', NomeCreen_view.as_view(), name='nomecreen_view'),
	url(r'^reporte/page/(?P<pagina>.*)/$', reporte, name='reporte_view'),
	url(r'^buscar/$', buscar, name='buscar_view'),
	url(r'^editar/$', editar, name='editar_view'),
	url(r'^detail/(?P<data_name>.*)/$', detail_view, name='detail_view'),
	url(r'^reporte2/$', Reporte2.as_view(), name='reporte2_view'),
	url(r'^detail_report/(?P<pk>\d+)$', Detail_report.as_view(), name='detail_reporte_view'),
	url(r'^reporte3/$', Reporte3.as_view(), name='reporte3_view'),
	
]