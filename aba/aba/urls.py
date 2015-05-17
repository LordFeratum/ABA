# INICIO FILES
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from aba import settings
# FIN FILES

from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from web.views import home, cargar_anuncios, contacto, enviarEmail, cargar_noticias

urlpatterns = patterns('',
    # Examples:
	url(r'^$', home),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^anuncios/', cargar_anuncios),
    url(r'^noticias/', cargar_noticias),
    url(r'^contacto/', contacto),
    url(r'^accounts/login/$', login, {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout, {'template_name': 'login.html'}),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
