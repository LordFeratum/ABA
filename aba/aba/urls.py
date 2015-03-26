from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.views import home

urlpatterns = patterns('',
    # Examples:
	url(r'^$', home),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
