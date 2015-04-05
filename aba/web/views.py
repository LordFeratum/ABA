# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.template import Template
from django.shortcuts import render_to_response, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
#from django.template.context_processors import csrf
from models import *

def home (request):
	return render_to_response('index.html', {'logueado' : request.user.is_authenticated(), 'usuario': request.user.username})


#Vista que devuelve una lista de anuncios ordenados por fecha.
def cargar_anuncios (request):
    anuncios_lista = Anuncio.objects.order_by("fechaPublicacion").reverse()
    return render_to_response('anuncios.html', {'anuncios' : anuncios_lista, 'logueado' : request.user.is_authenticated(), 
        'usuario': request.user.username})



@login_required
def publicar_anuncio (request):
    return HttpResponse("Anuncio publicado")


def contacto (request):
    contacto = Contacto.objects.all()[0];
    if request.method == 'POST':
        nombre = request.POST.get('name')
        email = request.POST.get('email')
        mensaje = request.POST.get('message')
        send_mail('ABA Contacto', mensaje, email, [contacto.email], fail_silently=False)
        
    return render_to_response('contacto.html', {'latitud' : contacto.latitud, 'longitud' : contacto.longitud, 'logueado' : request.user.is_authenticated(), 
        'usuario': request.user.username})


def enviarEmail (request):
    nombre = request.POST.get('name')
    email = request.POST.get('email')
    mensaje = request.POST.get('message')
    contacto = Contacto.objects.all()[0];
    send_mail('ABA Contacto', mensaje, email, [contacto.email], fail_silently=False)
    return render_to_response('contacto.html')
