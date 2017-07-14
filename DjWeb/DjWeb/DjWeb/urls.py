"""
Definition of urls for DjWeb.
"""

from django.conf.urls import include, url
from django.contrib import admin
from DjWeb.DjWebApp import views as my_views

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', DjWeb.views.home, name='home'),
    # url(r'^DjWeb/', include('DjWeb.DjWeb.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', my_views.hello, name = 'hello')
]
