#-*- coding:utf-8 -*-

from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('jstest.views',
    url(r'^qunit/(?P<app>[\w_]+)?$', 'suite_render'),
)