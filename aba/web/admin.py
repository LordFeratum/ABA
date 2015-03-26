from django.contrib import admin
from web.models import Anuncio, Noticia, Categoria, Documento


class AdminModel(admin.ModelAdmin):
	pass


admin.site.register(Anuncio, AdminModel)
admin.site.register(Noticia, AdminModel)
admin.site.register(Categoria, AdminModel)
admin.site.register(Documento, AdminModel)

# Register your models here.
