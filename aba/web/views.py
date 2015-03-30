# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.template import Template
from django.shortcuts import render_to_response, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from models import *

def home (request):
    if request.user.is_authenticated():
	   return render_to_response('index.html', {'logueado' : True})
    else:
        return render_to_response('index.html', {'logueado' : False})


# Create your views here.
def cargar_anuncios (request):
	anuncios_lista = Anuncio.objects.order_by("fechaPublicacion").reverse()
	# paginacion = Paginator(anuncios_lista, 10) #Habra 10 anuncios por pagina.

	# pagina = request.GET.get('page', 1) #Recojemos la pagina de la URL (la pasamos por GET)
 #    #anuncios = paginacion.page(page)
 #    try:
 #         anuncios = paginacion.page(pagina)
 #    except PageNotAnInteger:
 #         # Si la pagina no es un numero (en la URL) devolvemos la primera pagina
 #         anuncios = paginacion.page(1)
 #    except EmptyPage:
 #         # Si la pagina de la URL es un numero fuera del rango permitdo, mostraremos la utlima pagina
 #         anuncios = paginacion.page(paginacion.num_pages)

	return render_to_response('anuncios.html', {'anuncios' : anuncios_lista})


@login_required
def publicar_anuncio (request):
    return HttpResponse("Anuncio publicado")

