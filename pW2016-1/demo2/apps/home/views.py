#from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import Student
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
