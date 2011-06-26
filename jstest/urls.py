# coding: utf-8

from django.conf.urls.defaults import url, patterns
import os

media_root = os.path.join(os.path.dirname(__file__), 'media')
serve = 'django.views.static.serve'

urlpatterns = patterns('',
    # qunit
    url(r'^qunit/(?P<app>[\w_]+)?$', 'jstest.views.suite_render', {'framework': 'qunit'}),
    url(r'^qunit/qunit.js', serve, {'document_root': media_root, 'path': 'jstest/js/qunit/qunit.js'}, name='qunit_js'),
    url(r'^qunit/qunit.css', serve, {'document_root': media_root, 'path': 'jstest/css/qunit/qunit.css'}, name='qunit_css'),
    
    # jasmine
    url(r'^jasmine/(?P<app>[\w_]+)?$', 'jstest.views.suite_render', {'framework': 'jasmine'}),
)
