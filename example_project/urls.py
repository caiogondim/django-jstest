# coding: utf-8

from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import redirect_to

from jstest.conf import DEFAULT_FRAMEWORK


url_to_redirect = '/%s/' % DEFAULT_FRAMEWORK

urlpatterns = patterns('',
    (r'^/?$', redirect_to, {'url': url_to_redirect}),
    (r'^', include('jstest.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^mymedia/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )