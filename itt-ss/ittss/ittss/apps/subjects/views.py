from django.shortcuts import render
from django.views.generic import *

from ittss.apps.subjects.models import *
from ittss.apps.subjects.forms import *

class SubjectView(DetailView):
	model = Subject

class CreateSubjectView(CreateView):
	model = Subject
	form_class = CreateSubjectForm
	success_url = '/'
