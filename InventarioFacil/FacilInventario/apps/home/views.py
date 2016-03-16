from django.shortcuts import render
from django.views.generic import TemplateView
from apps.inventarios.models import Items
# Create your views here.

class Index_view(TemplateView):
	template_name = 'home/index_view.html'

def Test_view(request):

	
	if request.POST:
		inventario = request.POST['item']
		count = request.POST['cantidad']
		datos = request.POST['dia']
		vendedor = request.POST['chofer']
		#print inventario, count, datos, vendedor
		p = Items.objects.get(codigo=inventario)
		piezas = p.numero_piezas
		p.numero_piezas = piezas - (int(count))
		p.save()
		print piezas, type(int(count))
		ctx = {'item': inventario, 'cantidad': count, 'dia': datos, 'chofer': vendedor}
	else:
		ctx = {'mensaje': 'No Datos :('}
	return render(request, 'home/envio_datos_formulario.html', ctx)


	