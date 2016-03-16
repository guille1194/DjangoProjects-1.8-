from django.contrib import admin
from .models import Inventarios, Populares, Ventas
# Register your models here.
@admin.register(Inventarios)
class Instalacion_Admin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre', 'cantidad', 'costo_compra', 'costo_venta', 'stock', 'fecha')


@admin.register(Populares)
class Instalacion_Admin(admin.ModelAdmin):
	list_display = ('nombre', 'cantidad')


@admin.register(Ventas)
class Instalacion_Admin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre', 'cantidad', 'costo_venta', 'fecha')


