from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
	student_code = models.IntegerField()
	student_name = models.CharField(max_length=64)
	student_age = models.IntegerField()
	student_semester = models.IntegerField()
	student_career = models.CharField(max_length=64)
	student_image = models.ImageField(upload_to='student_perfil/', blank=True, null=True)
	slug = models.SlugField(blank=True, null=True)

	def __unicode__(self):
		return 'StudentCode: %s - StudentName: %s'%(self.student_code, self.student_name)


class Professor(models.Model):
	professor_name = models.CharField(max_length=64)
	class_room = models.IntegerField()
	students = models.ManyToManyField(Student)

	def __unicode__(self):
		return self.professor_name

	#def get_students(self):
	#	return "\n".join([p.student_name for p in self.students.all()])

class Perfil(models.Model):
	user_perfil = models.OneToOneField(User)
	mail = models.EmailField()
	phone = models.IntegerField()
	image = models.ImageField(upload_to='user_image', blank=True)

	def thumbnail(self):
		return '<a href="http://localhost:8000/media/%s"><img src="http://localhost:8000/media/%s" width=50px/></a>'%(self.image, self.image)
	thumbnail.allow_tags = True

