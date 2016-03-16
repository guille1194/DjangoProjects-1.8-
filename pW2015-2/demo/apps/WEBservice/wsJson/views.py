#from django.shortcuts import render

# Create your views here.
from apps.home.models import Personas

from django.core import serializers
from django.http import HttpResponse

def wsPersonas(request):
	data = serializers.serialize('json', Personas.objects.all())
	return HttpResponse(data, content_type='application/json')
