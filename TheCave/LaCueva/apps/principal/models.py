from django.db import models

# Create your models here.

class Inventarios(models.Model):
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=64)
	cantidad = models.IntegerField()
	costo_compra = models.FloatField()
	costo_venta = models.FloatField()
	stock = models.IntegerField()
	fecha = models.DateField(auto_now=True)

	def __unicode__(self):
		return "Codigo: %s Nombre: %s" %(self.codigo, self.nombre)



class Populares(models.Model):
	nombre = models.ForeignKey(Inventarios)
	cantidad = models.IntegerField()


	def __unicode__(self):
		return "Nombre: %s Cantidad: %d" %(self.Inventarios.nombre, self.cantidad)


class Ventas(models.Model):
	codigo = models.ForeignKey(Inventarios)
	nombre = models.CharField(max_length=64)
	cantidad = models.IntegerField()
	costo_venta = models.FloatField()
	fecha = models.DateField(auto_now=True)


	def __unicode__(self):
		return "Codigo: %d Nombre: %s Cantidad: %d" %(self.codigo, self.nombre, self.cantidad)


