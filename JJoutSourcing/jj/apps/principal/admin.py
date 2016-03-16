from django.contrib import admin
from .models import Instalacion, Inventarios, Tipo_servicio, Personal, Contrato, Ciudad, Compania

# Register your models here.
@admin.register(Instalacion)
class Instalacion_Admin(admin.ModelAdmin):
	list_display = ('contrato', 'tecnico', 'cliente', 'direccion', 'fecha_instalacion',)


#admin.site.register(Tipo_servicio)
#admin.site.register(Inventarios)


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
	list_display = ["codigo", "nombre", "compania", "ciudad", "fecha_ingreso"]
	#list_filter = ['fecha_ingreso',]
	#search_fields =["ciudad", "nombre", "codigo", "compania",]

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
	list_display = ["nombre", "codigo"]

@admin.register(Compania)
class CompaniaAdmin(admin.ModelAdmin):
	list_display = ["nombre", "codigo"]
	
@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
	list_display = ["codigo", "compania", "ciudad"]	

# @admin.register(Instalacion)
# class InstalacionAdmin(admin.ModelAdmin):
# 	list_display = ["codigo", "compania", "ciudad", "tecnico", "contrato", "tipo_instalacion","fecha_instalacion",]
# 	list_filter = ['fecha_instalacion', "tecnico",]

@admin.register(Inventarios)
class InventariosAdmin(admin.ModelAdmin):
	list_display = ["codigo", "nombre", "cantidad"]

@admin.register(Tipo_servicio)
class Tipo_servicio_Admin(admin.ModelAdmin):
	list_display = ["nombre", "pago"]
