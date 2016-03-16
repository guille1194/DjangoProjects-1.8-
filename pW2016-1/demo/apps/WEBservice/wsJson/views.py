#from django.shortcuts import render

# Create your views here.
from apps.home.models import Student

from django.core import serializers
from django.http import HttpResponse

def wsStudent(request):
	data = serializers.serialize('json', Student.objects.all())
	#print data
	return HttpResponse(data, content_type='application/json')
