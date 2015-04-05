from django.contrib import admin
from web.models import Anuncio, Noticia, Categoria, Documento, Contacto
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields


class AdminModel(admin.ModelAdmin):
	pass


class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
	    map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},    
	}


admin.site.register(Anuncio, AdminModel)
admin.site.register(Noticia, AdminModel)
admin.site.register(Categoria, AdminModel)
admin.site.register(Documento, AdminModel)
admin.site.register(Contacto, AdminModel)

# Register your models here.
