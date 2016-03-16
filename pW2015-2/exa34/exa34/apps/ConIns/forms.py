from django import forms

from .models import *
from exa34.apps.Usuario.models import *

class TipoInstalacionForm(forms.ModelForm):
	class Meta:
			model = TipoInstalacion
			fields = ['Nombre']

class ContratoForm(forms.ModelForm):
	class Meta:
			model = Contrato
			fields = ['Ciudad', 'Tipo_de_instalacion', 'Cliente']

class InstalacionForm(forms.ModelForm):
	class Meta:
			model = Instalacion
			fields = ['Usuario', 'Contrato']

class InventarioForm(forms.ModelForm):
	class Meta:
			model = Inventario
			fields = ['Nombre', 'Cantidad', 'Marca', 'Serial']

class InvInsForm(forms.ModelForm):
	class Meta:
			model = InvIns
			fields = ['Cantidad', 'Inventario', 'Instalacion']

class NomTec(forms.Form):
	Nombre = forms.ModelChoiceField(queryset=Usuario.objects.all().filter(Tipo_de_usuario=1))

	class Meta:
	    model = Instalacion
	    fields = '__all__'
