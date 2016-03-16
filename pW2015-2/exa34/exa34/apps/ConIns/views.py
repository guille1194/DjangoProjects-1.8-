from django.shortcuts import render

from .forms import *
from .models import *

# Create your views here.
def formContrato(request):
	form = ContratoForm(request.POST or None)
	ctx = {
		"form": form
	}

	if form.is_valid():
		form.save()
		form = ContratoForm()
		ctx = {
			"mensaje": "Guardado", "form": form
		}

	return render(request, "ConIns/formContrato_view.html", ctx)

def formInstalacion(request):
	form = InstalacionForm(request.POST or None)
	ctx = {
		"form": form
	}

	if form.is_valid():
		form.save()
		form = InstalacionForm()
		ctx = {
			"mensaje": "Guardado", "form": form
		}

	return render(request, "ConIns/formInstalacion_view.html", ctx)

def formTipoInstalacion(request):
	form = TipoInstalacionForm(request.POST or None)
	ctx = {
		"form": form
	}

	if form.is_valid():
		form.save()
		form = TipoInstalacionForm
		ctx = {
			"mensaje": "Guardado", "form": form
		}

	return render(request, "ConIns/formTipoInstalacion_view.html", ctx)

def formInventario(request):
	form = InventarioForm(request.POST or None)
	ctx = {
		"form": form
	}

	if form.is_valid():
		form.save()
		form = InventarioForm()
		ctx = {
			"mensaje": "Guardado", "form": form
		}

	return render(request, "ConIns/formInventario_view.html", ctx)

def formInvIns(request):
	form = InvInsForm(request.POST or None)
	ctx = {
		"form": form
	}

	if form.is_valid():
		data = form.cleaned_data
		query = Inventario.objects.get(Nombre = data['Inventario'])
		nuevoInv = query.Cantidad - data['Cantidad']
		if nuevoInv >= 0:
			query.Cantidad = nuevoInv
			query.save()
			form.save()
			form = InvInsForm()
			ctx = {
				"mensaje": "Guardado", "form": form
			}
		else: 
			ctx = {
				"mensaje": "No existe inventario suficiente", "form": form
			}

	return render(request, "ConIns/formInvIns_view.html", ctx)

def reporteInventario(request):
	query = Inventario.objects.all
	ctx = {"datos": query}
	return render(request, "ConIns/reportInv_view.html", ctx)

def reporteInstalacion(request):

	if request.POST:
		c = request.POST.get('contrato')
		update = Instalacion.objects.get(id=c)
		update.Aprobacion = True

		update.save()

		query = Instalacion.objects.all
		ctx={'datos':query}
		return render(request,'ConIns/reportInst_view.html',ctx)

	query = Instalacion.objects.all
	ctx = {"datos": query}
	return render(request, "ConIns/reportInst_view.html", ctx)

def reporteTecGen(request):
	query = Instalacion.objects.all().order_by('-Fecha')
	ctx = {"datos": query}
	return render(request, "ConIns/reportTecGen_view.html", ctx)

def reporteTecEsp(request):
	query = Instalacion.objects.all().order_by('-Fecha')
	form = NomTec()
	ctx = {"datos": query, 'form': form}
	

	if request.method == "POST":
		form =  NomTec(request.POST, request.FILES)
		if form.is_valid():
						
			nom = form.cleaned_data['Nombre'] 
			query = Instalacion.objects.all().filter(Usuario__Nombre=nom).order_by('-Fecha')
			
			ctx={'datos':query,'form':form}
			return render(request, 'ConIns/reportTecEsp_view.html',ctx)

		else:
			forms =  NomTec()

	return render(request, "ConIns/reportTecEsp_view.html", ctx)

def home(request):
	return render(request, "ConIns/index_view.html", {})