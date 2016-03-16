from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Empresa)