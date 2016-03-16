from django.shortcuts import render
from django.views.generic import FormView, TemplateView, CreateView, ListView, DetailView
#from django.http import HttpResponseRedirect
# Create your views here.
#############################
# -*- coding: utf-8 -*-

########################
from .models import Personas, NomeCreen
from .forms import Personas_Form, PersonasForm, Personas_FormSet
from django.core.urlresolvers import reverse_lazy

from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.forms.formsets import formset_factory
# class Index_view(TemplateView):
# 	template_name = 'home/index_view.html'

class Signup(TemplateView):
	template_name = 'home/signup.html'


class About_view(TemplateView):
	template_name = 'home/about_view.html'


class Datos_register(CreateView):
	template_name = 'home/datos.html'
	model = Personas
	#form_class = Personas_Form
	fields = ['employ_code', 'employ_name', 'employ_edad', 'employ_image']
	success_url = reverse_lazy('datos_view')


class NomeCreen_view(CreateView):
	template_name = 'home/nomecreen.html'
	model = NomeCreen
	fields = ['name', 'phone']
	success_url = reverse_lazy('reporte_view')

# def datos(request):
# 	#form = Personas_Form()
# 	if request.method == 'POST':
# 		form = Personas_Form(request.POST, request.FILES)
# 		if form.is_valid():
# 			e_code = form.cleaned_data['emp_code']
# 			e_name = form.cleaned_data['emp_name']
# 			e_age = form.cleaned_data['emp_age']
# 			e_date = form.cleaned_data['emp_date']
# 			e_image = form.cleaned_data['emp_image']

# 			p = Personas()
# 			p.employ_code = e_code
# 			p.employ_name = e_name
# 			p.employ_edad = e_age
# 			p.date = e_date
# 			p.employ_image = e_image

# 			p.save()
# 			#Personas.objects.create(employ_code=e_code, employ_name=e_name,
# 			#	employ_edad=e_age, date=e_date, employ_image=e_image)
# 			return HttpResponseRedirect('/dato/')
# 	else:
# 		form = Personas_Form()
# 	ctx = {'mensaje':'Datos Guardados', 'form': form}
# 	return render(request,'home/datos.html',ctx) 

class Reporte3(ListView):
	template_name = 'home/reporte3.html'
	model = Personas


def reporte(request, pagina):
	#query = Personas.objects.all().order_by('-employ_code')
	#unique_query = Personas.objects.get(employ_code=321)
	filter_query = Personas.objects.all()

	paginator = Paginator(filter_query,5)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		r = paginator.page(page)
	except (EmptyPage, InvalidPage):
		r = paginator.page(paginator.num_pages)

	ctx = {'filter':r}
	return render(request,'home/reporte.html',ctx)


def buscar(request):
	if request.POST:
		consulta = request.POST['buscar']
		query = Personas.objects.get(id=consulta)
	
		ctx = {'code': query}

	else:
		ctx = {'mensaje':'no hay datos..'}
	return render(request,'home/buscar.html',ctx)
	

def editar(request):
	if request.POST:
		code = request.POST['buscar']
		
	# 	age = request.POST['emp_age']
	# 	date = request.POST['emp_date']
	# 	p = Personas.objects.get(employ_code=code)
	# 	p.employ_code = code
	# 	p.employ_name = name
	# 	p.employ_edad = age
	# 	p.date = date
	# 	p.save()

	# 	ctx = {'datos': p}
	# else:
	# 	ctx = {'mensaje': 'Editar Registros'}
	return render(request, 'home/editar.html', {'codigo': code})


class Reporte2(ListView):
	template_name = 'home/reporte2.html'
	model = Personas


class Detail_report(DetailView):
	model = Personas
	template_name = 'home/detail_report.html'
	slug_field = 'employ_name'

def detail_view(request, data_name):
	if request.method=='GET':
		p = Personas.objects.get(employ_name=data_name)
		form = Personas_Form(initial={
			'emp_code':p.employ_code, 'emp_name':p.employ_name,
			'emp_age':p.employ_edad, 'emp_date':p.date, 'emp_image':p.employ_image
			})
		
	ctx = {'form':form}
	return render(request, 'home/detail.html', ctx)

class Detail2(DetailView):
	template_name = 'home/detail_report.html'
	model = Personas


class DatosFormSet(FormView):
	template_name = 'home/datos.html'
	form_class = formset_factory(Personas_FormSet, extra=2)
	success_url = '/dato/'

	def form_valid(self, form):
		for f in form:
			f.save()
		return super(DatosFormSet, self).form_valid(form)


class DatosSet(FormView):
	template_name = 'home/datos.html'
	form_class = formset_factory(PersonasForm, extra=2)
	success_url = '/'


	def form_valid(self, form):
		for f in form:
			f.save()
		return super(DatosSet, self).form_valid(form)








