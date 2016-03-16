from django.shortcuts import render

from .forms import *
from .models import *

# Create your views here.
def formUsuario(request):
	form = UsuarioForm(request.POST or None)
	ctx = {
		"form": form
	}

	if form.is_valid():
		form.save()
		form = UsuarioForm()
		ctx = {
			"mensaje": "Guardado", "form": form
		}

	return render(request, "Usuario/formUsuario_view.html", ctx)

def formTipoUsuario(request):
	form = TipoUsuarioForm(request.POST or None)
	ctx = {
		"form": form
	}

	if form.is_valid():
		form.save()
		form = TipoUsuarioForm()
		ctx = {
			"mensaje": "Guardado", "form": form
		}

	return render(request, "Usuario/formTipoUsuario_view.html", ctx)

def formCliente(request):
	form = ClienteForm(request.POST or None)
	ctx = {
		"form": form
	}

	if form.is_valid():
		form.save()
		form = ClienteForm()
		ctx = {
			"mensaje": "Guardado", "form": form
		}

	return render(request, "Usuario/formCliente_view.html", ctx)

def formEmpresa(request):
	form = EmpresaForm(request.POST or None)
	ctx = {
		"form": form
	}

	if form.is_valid():
		form.save()
		form = EmpresaForm()
		ctx = {
			"mensaje": "Guardado", "form": form
		}

	return render(request, "Usuario/formEmpresa_view.html", ctx)

def reporteUsuario(request):
	query = Usuario.objects.all
	ctx = {"datos": query}
	return render(request, "Usuario/reportUsu_view.html", ctx)

def home(request):
	return render(request, "Usuario/index_view.html", {})
