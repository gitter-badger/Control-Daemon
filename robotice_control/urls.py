import os

from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

from robotice_control.views import BaseApiView

admin.autodiscover()

urlpatterns = patterns('robotice_control',
    url(r'^doc/', include('django.contrib.admindocs.urls')),
    url(r'^', include(admin.site.urls)),
 	
 	url(r'^api/systems$', BaseApiView.as_view(), name='systems'),

) + staticfiles_urlpatterns()