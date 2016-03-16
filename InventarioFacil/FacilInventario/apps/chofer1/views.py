from django.shortcuts import render
from apps.inventarios.models import Items
from .models import Salida_chofer1, Rechazo_chofer1
# Create your views here.


def salida_chofer1_view(request):

	if request.POST:
		inventario = request.POST['item']
		count = request.POST['cantidad']
		datos = request.POST['dia']
		vendedor = request.POST['chofer']
		#print inventario, count, datos, vendedor
		Salida_chofer1.objects.create(codigo_s=inventario, cantidad_s=count, fecha_s=datos)
		p = Items.objects.get(codigo=inventario)
		piezas = p.numero_piezas
		p.numero_piezas = piezas - (int(count))
		p.save()
		print piezas, type(int(count))
		ctx = {'item': inventario, 'cantidad': count, 'dia': datos, 'chofer': vendedor}
	else:
		ctx = {'mensaje': 'No Datos :('}
	return render(request, 'home/envio_datos_formulario.html', ctx)



def rechazo_chofer1_view(request):
	
	if request.POST:
		inventario = request.POST['item']
		count = request.POST['cantidad']
		datos = request.POST['dia']
		vendedor = request.POST['chofer']
		#print inventario, count, datos, vendedor
		Rechazo_chofer1.objects.create(codigo_r=inventario, cantidad_r=count, fecha_r=datos)
		p = Items.objects.get(codigo=inventario)
		piezas = p.numero_piezas
		p.numero_piezas = piezas + (int(count))
		p.save()
		print piezas, type(int(count))
		ctx = {'item': inventario, 'cantidad': count, 'dia': datos, 'chofer': vendedor}
	else:
		ctx = {'mensaje': 'No Datos :('}
	return render(request, 'home/envio_datos_formulario.html', ctx)

