from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Tecnico(models.Model):
# 	codigo = models.IntegerField()
# 	nombre = models.CharField(max_length=64)
# 	ciudad = models.CharField(max_length=64)
# 	cia = models.CharField(max_length=64)

# 	def __unicode__(self):
# 		return self.nombre

class Inventarios(models.Model):
	codigo = models.IntegerField(blank=True)
	nombre = models.CharField(max_length=48)
	cantidad = models.IntegerField()

	def __unicode__(self):
		return self.nombre

class Tipo_servicio(models.Model):
	nombre = models.CharField(max_length=256)
	pago = models.IntegerField()

	def __unicode__(self):
		return "%s %d"%(self.nombre, self.pago)



class Ciudad(models.Model):
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Compania(models.Model):
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

class Personal(models.Model):
	codigo = models.IntegerField()
	nombre = models.OneToOneField(User)
	compania = models.ForeignKey(Compania)
	ciudad = models.ForeignKey(Ciudad)
	fecha_ingreso = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return str(self.nombre.username)

class Contrato(models.Model):
	codigo = models.IntegerField()
	compania =  models.ForeignKey(Compania)
	ciudad = models.ForeignKey(Ciudad)

	def __unicode__(self):
		return str(self.codigo)



class Instalacion(models.Model):
	tecnico = models.ForeignKey(Personal)
	contrato = models.ForeignKey(Contrato)
	cliente = models.CharField(max_length=64)
	direccion = models.CharField(max_length=240)
	tipo_servicio = models.ManyToManyField(Tipo_servicio, related_name='payment')
	equipo_instalado = models.ManyToManyField(Inventarios)
	cantidad_equipo = models.IntegerField(blank=True)
	cantidad_tv = models.IntegerField(blank=True)
	observaciones = models.TextField(blank = True)
	fecha_instalacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return '%s - %s > %s'%(str(self.contrato), self.cliente, str(self.tipo_servicio))

# class Instalacion(models.Model):
# 	codigo = models.IntegerField()
# 	compania =  models.ForeignKey(Compania)
# 	ciudad = models.ForeignKey(Ciudad)
# 	tecnico = models.ForeignKey(Personal)
# 	contrato = models.ForeignKey(Contrato)
# 	fecha_instalacion = models.DateField(auto_now_add=True)
# 	tipo_instalacion = models.CharField(max_length=1)
# 	estatus = models.BooleanField(default=False)

# 	def __unicode__(self):
# 		return str(self.codigo)

# class Inventarios(models.Model):
# 	codigo = models.IntegerField()
# 	nombre =  models.CharField(max_length=250)
# 	cantidad = models.IntegerField()
# 	fecha_ingreso = models.DateField(auto_now_add=True)

# 	def __unicode__(self):
# 		return self.nombre


