from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(TipoInstalacion)
admin.site.register(Instalacion)
admin.site.register(Contrato)
admin.site.register(Inventario)
admin.site.register(InvIns)