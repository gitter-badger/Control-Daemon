import os

from django.conf.urls.defaults import url, patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

admin.autodiscover()

urlpatterns = patterns('meshlib.views',
    url(r'^doc/', include('django.contrib.admindocs.urls')),
     url(r'^', include(admin.site.urls)),

) + staticfiles_urlpatterns()