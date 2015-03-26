from django.contrib import admin
from web.models import Anuncio, Noticia


class AdminModel(admin.ModelAdmin):
	pass


admin.site.register(Anuncio, AdminModel)
admin.site.register(Noticia, AdminModel)

# Register your models here.
