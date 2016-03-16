from django.db import models

# Create your models here.

class Salida_chofer1(models.Model):
	codigo_s = models.CharField(max_length=8)
	cantidad_s = models.IntegerField()
	fecha_s = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return 'Codigo: %s -- Cantidad: %s -- Fecha: %s'%(self.codigo_s, self.cantidad_s, self.fecha_s)


class Rechazo_chofer1(models.Model):
	codigo_r = models.CharField(max_length=8)
	cantidad_r = models.IntegerField()
	fecha_r = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return 'Codigo: %s -- Cantidad: %s -- Fecha: %s'%(self.codigo_r, self.cantidad_r, self.fecha_r)
	