from django import forms

from .models import *

class TipoUsuarioForm(forms.ModelForm):
	class Meta:
			model = TipoUsuario
			fields = ['Nombre']

class UsuarioForm(forms.ModelForm):
	class Meta:
			model = Usuario
			fields = ['Nombre', 'Apellidos', 'Ciudad', 'Telefono','Correo', 'Tipo_de_usuario', 'Empresa' ]

class EmpresaForm(forms.ModelForm):
	class Meta:
			model = Empresa
			fields = ['Nombre', 'RFC', 'Direccion', 'Telefono']

class ClienteForm(forms.ModelForm):
	class Meta:
			model = Cliente
			fields = ['Nombre', 'Apellidos', 'Domicilio', 'Telefono','Correo']