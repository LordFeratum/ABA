from django.db import models

# Creamos los modelos. La base de datos constara de tres tabals sin relacion.

class Anuncio (models.Model):
	titulo = models.CharField(max_lenght=256)
	texto = models.TextField()
	fechaPublicacion = models.DateField()
	nick = models.CharField(max_lenght=50)


class Noticia (models.Model):
	titulo = models.CharField(max_lenght=256)
	texto = models.TextField()
	fechaPublicacion = models.DateField()