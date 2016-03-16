from django.contrib import admin
from .models import Personas, Perfiles, NomeCreen


# Register your models here.
@admin.register(Personas)
class Personas_admin(admin.ModelAdmin):
    list_display = ('employ_code', 'employ_name', 'employ_edad', 'date', 'employ_image', 'thumbnail',)
    list_filter = ('employ_code',)
    search_fields = ('employ_code', 'employ_name',)


@admin.register(Perfiles)
class Personas_admin(admin.ModelAdmin):
    list_display = ('usuario', 'phone', 'image', 'thumbnail',)
    #list_filter = ('employ_code',)
    #search_fields = ('employ_code', 'employ_name',)


@admin.register(NomeCreen)
class Personas_admin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    #list_filter = ('employ_code',)
    #search_fields = ('employ_code', 'employ_name',)



#admin.site.register(Personas)








