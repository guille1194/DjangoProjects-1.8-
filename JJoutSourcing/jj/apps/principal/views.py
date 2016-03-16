from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
# Create your views here.
# from django.views.generic import TemplateView
from .models import Instalacion #Personal
from forms import Instalacion_Form
#from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# def perfil_view(request):
# 	t = User.objects.get()
# 	p = Personal.objects.get(nombre=User.username)
# 	ctx = {'result': p}
# 	return render(request, 'principal/perfil.html', ctx)

#@login_required
def Instalacion_view(request):
	estado = False
	form = Instalacion_Form(request.POST or None)
	ctx = {"form": form, 'status': estado}

	if form.is_valid():
		form.save()
		estado = True
		form = Instalacion_Form()
		ctx = {"form": form, 'status': estado}
		print estado
	return render(request, 'principal/instalacion.html', ctx)

#@login_required
def buscar_view(request):
	if request.POST:
		fi = request.POST['fecha_inicio']
		ff = request.POST['fecha_final']
		t = str(request.POST['tecnico'])
		p = User.objects.get(username=t)
		#print fi, ff, t, type(t), p.id
		ctx = {'r':Instalacion.objects.filter(fecha_instalacion__range=(fi, ff)).filter(tecnico=p.id)}
		
	else:
		ctx = {'msg':'No hay Fecha'}
	return render(request, 'principal/buscar.html', ctx)

#@login_required
def reporteTecnico_view(request):
	if request.POST:
		t = request.POST['nombre_tecnico']
		q = User.objects.get(username=t)
		p = Instalacion.objects.filter(tecnico=q.id)
		ctx = {'tecnico':p}
	else:
		ctx = {'msg':'No hay Fecha'}
	return render(request, 'principal/reporteTecnico.html', ctx)

#@login_required
def pagoTecnico_view(request):
	if request.POST:
		fi = request.POST['fecha_inicio']
		ff = request.POST['fecha_final']
		t = str(request.POST['tecnico'])
		p = User.objects.get(username=t)
		result = Instalacion.objects.filter(fecha_instalacion__range=(fi, ff)).filter(tecnico=p.id)
		pago_tecnico = 0
		for x in result:
			for j in x.tipo_servicio.all():
				pago_tecnico = pago_tecnico + j.pago
		
		ctx = {'r':result, 'p_tecnico': pago_tecnico}
	else:
		ctx = {'msg':'No hay datos'}
	return render(request, 'principal/pago_tecnico.html', ctx)
