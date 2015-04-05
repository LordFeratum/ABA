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
#from django.core.context_processors import csrf


from models import *


def home(request):
    logueado = request.user.is_authenticated()
    usuario = request.user.username
    return render_to_response('index.html', locals())


#Vista que devuelve una lista de anuncios ordenados por fecha.
def cargar_anuncios (request):
    anuncios = Anuncio.objects.order_by("fechaPublicacion").reverse()
    logueado = request.user.is_authenticated()
    usuario = request.user.username
    return render_to_response('anuncios.html', locals())



@login_required
def publicar_anuncio (request):
    return HttpResponse("Anuncio publicado")


def contacto(request):
    contact = Contacto.objects.all()[0]
    if request.method == 'POST':
        # c = {}
        # c.update(csrf(request))


        nombre = request.POST.get('name')
        email = request.POST.get('email')
        mensaje = request.POST.get('message')
        send_mail('ABA Contacto', mensaje, email, [contact.email], fail_silently=False)
        #return HttpResponse('Guapo.')

    latitud = contact.latitud
    longitud = contact.longitud
    logueado = request.user.is_authenticated()
    usuario = request.user.username

    return render_to_response('contacto.html', locals())


def enviarEmail (request):
    nombre = request.POST.get('name')
    email = request.POST.get('email')
    mensaje = request.POST.get('message')
    contacto = Contacto.objects.all()[0]
    send_mail('ABA Contacto', mensaje, email, [contacto.email], fail_silently=False)
    return render_to_response('contacto.html')
