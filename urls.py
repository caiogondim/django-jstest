# coding: utf-8
from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^', include('jstest.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^mymedia/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )