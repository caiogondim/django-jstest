# coding: utf-8

from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import redirect_to


urlpatterns = patterns('',
    (r'^/?$', redirect_to, {'url': '/qunit/'}),
    (r'^', include('jstest.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
