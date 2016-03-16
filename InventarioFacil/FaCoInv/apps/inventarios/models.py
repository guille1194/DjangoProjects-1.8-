from django.db import models

# Create your models here.

class Items(models.Model):
    codigo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=64)
    numero_piezas = models.IntegerField()
    unidad_medida = models.CharField(max_length=2)
    gramaje = models.FloatField()
    familia = models.CharField(max_length=24)
    precio_lista = models.FloatField()
    descuento_oferta = models.FloatField()
    precio_factura = models.FloatField()
    margen_ganancia_sugerido = models.FloatField()
    precio_sugerido = models.FloatField()
    fecha_entrada = models.DateField(auto_now_add=True)
    fecha_caducidad = models.DateField(auto_now_add=False)


    def __unicode__(self):
        return "codigo: %s; nombre:  %s; caducidad: %s"%(self.codigo, self.nombre, self.fecha_caducidad)


