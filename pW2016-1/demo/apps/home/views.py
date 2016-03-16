from django.shortcuts import render
from django.views.generic import FormView, CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Student, Perfil, Professor
from .forms import User_form
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.


class About(TemplateView):
	template_name = 'home/about.html'


class Student_register(CreateView):
	template_name = 'home/register.html'
	model = Student
	fields = ['student_code', 'student_name', 'student_age', 'student_semester', 'student_career', 'student_image']
	success_url = reverse_lazy('register_student_view')


class StudentsReport(ListView):
	template_name = 'home/students_report.html'
	model = Student


class PerfilReport(ListView):
	template_name = 'home/perfil_report.html'
	model =  Perfil


def buscar(request):
	if request.POST:
		data = request.POST['campo']
		p = Student.objects.filter(student_semester=data)
		ctx = {'objects': p} 
	else:
		ctx = {'mensaje':'no hay datos..'}
	return render(request, 'home/buscar.html', ctx)


class Detail_view(DetailView):
	model = Student
	template_name = 'home/detail.html'
	slug_field = 'student_name'

class Signup(FormView):
	template_name = 'home/signup.html'
	form_class = User_form
	#fields = ['user_perfil', 'mail', 'phone']
	success_url = reverse_lazy('signup_view')


	def form_valid(self, form):
		user = form.save()
		p = Perfil()
		p.user_perfil = user
		p.mail = form.cleaned_data['mail']
		p.phone = form.cleaned_data['phone']
		p.save()
		return super(Signup, self).form_valid(form)



class Update_view(UpdateView):
	model = Student
	fields = '__all__'
	template_name = 'home/update_view.html'
	success_url = reverse_lazy('student_report_view')


# class Update_view(UpdateView):
# 	model = Student
# 	fields = ['student_code', 'student_name', 'student_age', 'student_semester', 'student_career', 'student_image']
# 	template_name = 'home/update_view.html'
# 	success_url = reverse_lazy('student_report_view')

class Delete_view(DeleteView):
	model = Student
	fields = '__all__'
	template_name = 'home/delete_view.html'
	success_url = reverse_lazy('student_report_view')


class Register_professor(CreateView):
	template_name = 'home/Register_professor.html'
	model = Professor
	fields = '__all__'
	success_url = reverse_lazy('report_professor_view')

class Report_professor(ListView):
	template_name = 'home/Report_professor.html'
	model = Professor


def paginator_report(request, pagina):
	#query = Personas.objects.all().order_by('-employ_code')
	#unique_query = Personas.objects.get(employ_code=321)
	filter_query = Student.objects.all()

	paginator = Paginator(filter_query,3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		r = paginator.page(page)
	except (EmptyPage, InvalidPage):
		r = paginator.page(paginator.num_pages)

	ctx = {'filter':r}
	return render(request,'home/paginator_report.html',ctx)


