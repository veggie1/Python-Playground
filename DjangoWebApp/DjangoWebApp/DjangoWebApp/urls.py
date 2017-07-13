"""
Definition of urls for DjangoWebApp.
"""

from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from DjangoWebApp.myApp import views as myapp_views

urlpatterns = [
    # Examples:
    # url(r'^$', DjangoWebApp.views.home, name='home'),
    # url(r'^DjangoWebApp/', include('DjangoWebApp.DjangoWebApp.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', myapp_views.hello, name = 'hello')
]
