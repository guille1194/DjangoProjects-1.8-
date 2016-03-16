from django import forms
from .models import Inventarios


class Inventarios_form(forms.ModelForm):
	class Meta:
		model = Inventarios
		fields = ['codigo', 'nombre', 'cantidad', 'costo_compra', 'costo_venta', 'stock']
