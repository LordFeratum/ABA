# INICIO FILES
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from aba import settings
# FIN FILES

from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.views import home, cargar_anuncios

urlpatterns = patterns('',
    # Examples:
	url(r'^$', home),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^anuncios/(?P<pagina>\w{0,50})/$', cargar_anuncios), 
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
