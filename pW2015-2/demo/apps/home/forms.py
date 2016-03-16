from django import forms
from .models import Personas

class Personas_Form(forms.Form):
	emp_code = forms.IntegerField()
	emp_name = forms.CharField()
	emp_age = forms.IntegerField()
	#emp_date = forms.DateField()
	emp_image = forms.ImageField()


class PersonasForm(forms.ModelForm):
	class Meta:
		model = Personas
		fields = ('employ_code', 'employ_name', 'employ_edad', 'employ_image')

	def clean_employ_code(self):
		emp_code = self.cleaned_data['employ_code']
		if type(emp_code) == int:
			return self.cleaned_data['employ_code']
		else:
			self.add_error('employ_code', 'error en codigo, solo numeros')

	def clean_name(self):
		name = self.cleaned_data['employ_name']
		if name == name.upper():
			self.add_error('name', 'Error, no todo se escribe en mayuscula')
		else:
			return self.cleaned_data['name']




class Personas_FormSet(forms.ModelForm):
	class Meta:
		model = Personas
		fields = ('employ_code', 'employ_name', 'employ_edad', 'employ_image')
		