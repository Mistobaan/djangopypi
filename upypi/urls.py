from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^pypi/', include('djangopypi.urls')),
                       url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'amxpypi.views.home', name='home'),
    # url(r'^amxpypi/', include('amxpypi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
