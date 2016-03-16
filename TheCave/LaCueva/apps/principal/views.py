from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Inventarios

# Create your views here.


class Inventarios_view(CreateView):
	template_name = 'principal/inventarios_view.html'
	model = Inventarios
	fields = ['codigo', 'nombre', 'cantidad', 'costo_compra', 'costo_venta', 'stock']
	success_url = reverse_lazy('inventarios_view')


	def post(self, request, *args, **kwargs):
		estado = False
		item = Inventarios()
		item.codigo = request.POST['codigo']
		item.nombre = request.POST['nombre']
		item.cantidad = request.POST['cantidad']
		item.costo_compra = request.POST['costo_compra']
		item.costo_venta = request.POST['costo_venta']
		item.stock = request.POST['stock']
		item.save()
		estado = True
		ctx = {'status': estado}
		return render(request, 'principal/inventarios_view.html', ctx)
# def inventarios_view(request):
# 	estado = False
# 	form = Inventarios_form(request.POST or None)
# 	ctx = {"form": form, 'status': estado}

# 	if form.is_valid():
# 		form.save()
# 		estado = True
# 		form = Inventarios_form()
# 		ctx = {"form": form, 'status': estado}
# 		print estado
# 	return render(request, 'principal/inventarios_view.html', ctx)

def ventas_view(request):
	return render(request, 'principal/ventas_view.html')

def populares_view(request):
	return render(request, 'principal/populares_view.html')

def reporte_ventas_periodo_view(request):
	return render(request, 'principal/reporte_ventas_periodo_view.html')

def reporte_ventas_dia_view(request):
	return render(request, 'principal/reporte_ventas_dia_view.html')

def consulta_view(request):
	return render(request, 'principal/consulta_view.html')
