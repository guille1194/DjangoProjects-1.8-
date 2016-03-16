from django.shortcuts import render
#from .views import reporte_chofer1_view
from apps.chofer1.models import Salida_chofer1, Rechazo_chofer1
# Create your views here.

def reporte_chofer1_view(request):
	if request.POST:
		inventario = request.POST['item']
		count = request.POST['cantidad']
		datos = request.POST['dia']
		vendedor = request.POST['chofer']
		s = Salida_chofer1.objects.filter(fecha_s=datos)
		r = Rechazo_chofer1.objects.filter(fecha_r=datos)
		j=0
		for i in s:
			q = i.cantidad_s
			j = j + q
		print s, '.>', r[0].cantidad_r 
		print j
		
		ctx = {'item': inventario, 'cantidad': count, 'dia': datos, 'chofer': vendedor}
	else:
		ctx = {'mensaje': 'No Datos :('}
	return render(request, 'home/envio_datos_formulario.html', ctx)
