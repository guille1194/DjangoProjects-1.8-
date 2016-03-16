from django.forms import ModelForm
from ittss.apps.subjects.models import *

class CreateSubjectForm(ModelForm):
	class Meta:
		model = Subject

	def __init__(self, *args, **kwargs):
		super(CreateSubjectForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'