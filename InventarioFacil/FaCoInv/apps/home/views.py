from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Index_view(TemplateView):
	template_name = 'home/index_view.html'

def Test_view(request):

	dic = {}
	if request.POST:
		inventario = request.POST['item']
		count = request.POST['cantidad']
		datos = request.POST['dia']
		vendedor = request.POST['chofer']
		#print inventario, count, datos, vendedor
		dic[inventario] = count 
		print dic
		ctx = {'item': inventario, 'cantidad': count, 'dia': datos, 'chofer': vendedor}
	else:
		ctx = {'mensaje': 'No Datos :('}
	return render(request, 'home/envio_datos_formulario.html', ctx)