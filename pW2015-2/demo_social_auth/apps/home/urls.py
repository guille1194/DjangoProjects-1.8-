from django.conf.urls import url
from .views import Index #About_view, Datos_register, NomeCreen_view, reporte, buscar, editar, detail_view, Signup
urlpatterns = [
	
	url(r'^$', Index.as_view(), name='index_view'),
	# url(r'^$', 'django.contrib.auth.views.login', {'template_name':'home/index_view.html'}, name='login'),
	# url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
	# url(r'^signup/$', Signup.as_view(), name='signup_view'),
	# url(r'^about/$', About_view.as_view(), name='about_view'),
	# url(r'^dato/$', Datos_register.as_view(), name='datos_view'),
	# url(r'^nomecreen/$', NomeCreen_view.as_view(), name='nomecreen_view'),
	# url(r'^reporte/$', reporte, name='reporte_view'),
	# url(r'^buscar/$', buscar, name='buscar_view'),
	# url(r'^editar/$', editar, name='editar_view'),
	# url(r'^detail/(?P<data_name>.*)/$', detail_view, name='detail_view'),
]