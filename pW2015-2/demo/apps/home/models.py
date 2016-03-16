from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Personas(models.Model):
	employ_code = models.IntegerField()
	employ_name = models.CharField(max_length=48)
	employ_edad = models.IntegerField()
	date = models.DateField(auto_now_add=True)
	employ_image = models.ImageField(upload_to='employ_image')


	def __unicode__(self):
		return " Employ Code: %d; Employ Name: %s; Date: %s"%(self.employ_code, self.employ_name, self.date)

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px/></a>'%(self.employ_image, self.employ_image)
	thumbnail.allow_tags = True		

class Perfiles(models.Model):
	usuario = models.OneToOneField(User)
	phone = models.IntegerField()
	image = models.ImageField(upload_to='user_image', blank=True)

	def __unicode__(self):
		return self.usuario.username


	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px/></a>'%(self.image, self.image)
	thumbnail.allow_tags = True	




class NomeCreenQuerySet(models.QuerySet):
	def boys(self):
		return self.filter(male=True)

	def girls(self):
		return self.filter(male=False)

class NomeCreen(models.Model):
	name = models.CharField(max_length=24)
	phone = models.IntegerField()
	male = models.BooleanField(default=True)
	p = NomeCreenQuerySet.as_manager()
	people = models.Manager()


	def __unicode__(self):
		return self.name

class TestMultiDataSet(models.Model):
	name = models.CharField(max_length=12)
	phone = models.CharField(max_length=12)

	def __unicode__(self):
		return self.name



