from django.db import models

# Creamos los modelos. La base de datos constara de tres tabals sin relacion.

class Anuncio (models.Model):
	titulo = models.CharField(max_length=256)
	texto = models.TextField()
	fechaPublicacion = models.DateField()
	nick = models.CharField(max_length=50)
	imagen = models.ImageField(upload_to='images', null=True)


class Noticia (models.Model):
	titulo = models.CharField(max_length=256)
	texto = models.TextField()
	fechaPublicacion = models.DateField()
	imagen = models.ImageField(upload_to='images', null=True)
