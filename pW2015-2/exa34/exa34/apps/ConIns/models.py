from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class TipoInstalacion(models.Model):
	Nombre = models.CharField(max_length = 96)
	FecAct = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return u'%s' % (self.Nombre)

class Contrato(models.Model):
	NumCont = models.AutoField(_('No. de contrato'), primary_key = True)
	Ciudad = models.CharField(max_length = 96)
	Tipo_de_instalacion = models.ForeignKey('TipoInstalacion')
	Fecha= models.DateField(auto_now_add = True)
	Cliente= models.OneToOneField('Usuario.Cliente')
	FecAct = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return u'%d %s' % (self.NumCont, self.Cliente)

class Instalacion(models.Model):
	Aprobacion = models.BooleanField(default= False)
	Fecha = models.DateField(auto_now_add = True)
	Usuario = models.ForeignKey('Usuario.Usuario', limit_choices_to={'Tipo_de_usuario': 1})
	Contrato = models.ForeignKey('Contrato')
	FecAct = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return u'%s %s %s' % (self.Contrato, self.Usuario, self.Fecha)

class Inventario(models.Model):
	Nombre = models.CharField(max_length = 96)
	Cantidad = models.PositiveIntegerField()
	Marca = models.CharField(max_length = 96)
	Serial = models.CharField(max_length = 96)
	FecAct = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return u'%s' % (self.Nombre)

class InvIns(models.Model):
	Cantidad = models.PositiveIntegerField()
	Fecha = models.DateField(auto_now_add = True)
	Inventario= models.ForeignKey('Inventario')
	Instalacion= models.ForeignKey('Instalacion') 
	FecAct = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return u'%d' % (self.id)