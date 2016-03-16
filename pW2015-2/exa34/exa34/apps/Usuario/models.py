from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class TipoUsuario(models.Model):
	Nombre = models.CharField(max_length = 96)
	FecAct = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.Nombre

class Usuario(models.Model):
	Matricula = models.AutoField(primary_key = True)
	Nombre= models.CharField(max_length = 96)
	Apellidos= models.CharField(max_length = 96)
	Ciudad = models.CharField(max_length = 96)
	Telefono = models.IntegerField()
	Correo = models.EmailField(max_length = 96)
	Tipo_de_usuario = models.ForeignKey('TipoUsuario')
	Empresa = models.ForeignKey('Empresa')
	FecAct = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.Nombre

class Cliente(models.Model):
	Nombre= models.CharField(max_length = 96)
	Apellidos= models.CharField(max_length = 96)
	Domicilio = models.CharField(max_length = 96)
	Telefono = models.IntegerField()
	Correo = models.EmailField(max_length = 96)
	FecAct = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.Nombre

class Empresa(models.Model):
	Nombre= models.CharField(max_length = 96)
	RFC= models.CharField(max_length = 96)
	Direccion = models.CharField(max_length = 96)
	Telefono = models.IntegerField()
	FecAct = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.Nombre