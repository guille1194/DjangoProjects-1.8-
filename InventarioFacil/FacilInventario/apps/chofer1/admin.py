from django.contrib import admin
from .models import Salida_chofer1, Rechazo_chofer1

@admin.register(Salida_chofer1)
class Salida_chofer1_admin(admin.ModelAdmin):
    list_display = ('codigo_s', 'cantidad_s', 'fecha_s',)
    list_filter = ('codigo_s',)
    search_fields = ('codigo_s', 'fecha_s')

@admin.register(Rechazo_chofer1)
class Rechazo_chofer1_admin(admin.ModelAdmin):
    list_display = ('codigo_r', 'cantidad_r', 'fecha_r',)
    list_filter = ('codigo_r',)
    search_fields = ('codigo_r', 'fecha_r')
