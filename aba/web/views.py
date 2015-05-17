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
from django.shortcuts import render
from web.models import Anuncio, Noticia
from web.forms import ContactoForm, AnuncioForm
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage


from models import *


def home(request):
    logueado = request.user.is_authenticated()
    usuario = request.user.username
    return render_to_response('index.html', locals())

@csrf_protect
def cargar_noticias(request):
    logueado = request.user.is_authenticated()

    if(logueado):
        if request.method == 'POST':
            form = AnuncioForm(request.user.username, request.POST, request.FILES)

            if form.is_valid():
                form.save()

        else:
            form = AnuncioForm(request.user.username)

    anuncios_noticias = Noticia.objects.order_by("fechaPublicacion").reverse()

    #PAGINACION
    paginator = Paginator(anuncios_noticias, 10)
    page = request.GET.get('page')

    try:
        ads = paginator.page(page)

    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    #FIN PAGINACION

    usuario = request.user.username
    return render_to_response('anuncios_noticias.html', locals(), context_instance=RequestContext(request))


#Vista que devuelve una lista de anuncios ordenados por fecha.
@csrf_protect
def cargar_anuncios(request):
    logueado = request.user.is_authenticated()

    if (logueado):
        if request.method == 'POST':
            form = AnuncioForm(request.user.username, request.POST, request.FILES)

            if form.is_valid():
                form.save()
                
        else:
            form = AnuncioForm(request.user.username)

    anuncios_noticias = Anuncio.objects.order_by("fechaPublicacion").reverse()

    #PAGINACION
    paginator = Paginator(anuncios_noticias, 10)
    page = request.GET.get('page')

    try:
        ads = paginator.page(page)

    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    #FIN PAGINACION

    usuario = request.user.username
    return render_to_response('anuncios_noticias.html', locals(), context_instance=RequestContext(request))


@login_required
def publicar_anuncio(request):
    return HttpResponse("Anuncio publicado")


@csrf_protect
def contacto(request):
    contact = Contacto.objects.all()[0]
    if request.method == 'POST':
        # c = {}
        # c.update(csrf(request))
        form = ContactoForm(request.POST)

        nombre = request.POST.get('name', '')
        email = request.POST.get('email', '')
        mensaje = request.POST.get('message', '')

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            recipients = [contact.email]
            #recipients.append(email)

            send_mail('ABA Contacto', mensaje, email, recipients, fail_silently=False)
    else:
        form = ContactoForm()        

    latitud = contact.latitud
    longitud = contact.longitud
    logueado = request.user.is_authenticated()
    usuario = request.user.username

    return render_to_response('contacto.html', locals(), context_instance=RequestContext(request))


def enviarEmail (request):
    nombre = request.POST.get('name')
    email = request.POST.get('email')
    mensaje = request.POST.get('message')
    contacto = Contacto.objects.all()[0]
    send_mail('ABA Contacto', mensaje, email, [contacto.email], fail_silently=False)
    return render_to_response('contacto.html')
