from django.db import models

# Create your models here.

class Empleado(models.Model):
	codigo = models.CharField(max_length=5)
	nombre = models.CharField(max_length=48)
	direccion = models.CharField(max_length=120)
	telefono = models.CharField(max_length=13)
	nss = models.CharField(max_length=11)
	