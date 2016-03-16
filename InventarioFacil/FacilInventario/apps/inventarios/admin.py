from django.contrib import admin
from .models import Items

@admin.register(Items)
class Items_admin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'numero_piezas', 'unidad_medida', 'gramaje', 'familia', 'precio_lista', 'precio_factura', 'precio_sugerido', 'fecha_caducidad',)
    list_filter = ('codigo', 'nombre', 'familia', )
    search_fields = ('codigo', 'nombre', )


#admin.site.register(Items, Items_admin)