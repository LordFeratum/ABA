from django.db import models

# Creamos los modelos. La base de datos constara de tres tabals sin relacion.

class Anuncio (models.Model):
	titulo = models.CharField(max_length=256)
	texto = models.TextField()
	fechaPublicacion = models.DateTimeField()
	nick = models.CharField(max_length=50)
	imagen = models.ImageField(upload_to='files/images/anuncios', null=True)

	def __str__(self):         
		return self.titulo


class Noticia (models.Model):
	titulo = models.CharField(max_length=256)
	texto = models.TextField()
	fechaPublicacion = models.DateTimeField()
	imagen = models.ImageField(upload_to='files/images/noticias', null=True)

	def __str__(self):         
		return self.titulo


class Categoria (models.Model):
	titulo = models.CharField(max_length=256)
	
	def __unicode__(self):         
		return self.titulo

	def __str__(self):         
		return self.titulo  


class Documento (models.Model):
	nombre = models.CharField(max_length=256)	
	fechaPublicacion = models.DateTimeField()
	archivo = models.FileField(upload_to='files/documents', null=False)
	categoria = models.ForeignKey ('Categoria')

	def __str__(self):         
		return self.nombre
