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


	def __unicode__(self):
		return 'StudentCode: %s - StudentName: %s'%(self.student_code, self.student_name)



class Perfil(models.Model):
	user_perfil = models.OneToOneField(User)
	mail = models.EmailField()
	phone = models.IntegerField()


	def __unicode__(self):
		return self.user_perfil.username