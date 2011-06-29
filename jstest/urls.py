# coding: utf-8

from django.conf.urls.defaults import url, patterns
import os


media_root = os.path.join(os.path.dirname(__file__), 'jstest_media')
serve = 'django.views.static.serve'

urlpatterns = patterns('',
    # qunit
    url(r'^qunit/(?P<app>[\w_]+)?$', 'jstest.views.suite_render', {'framework': 'qunit'}),
    url(r'^qunit/qunit.js', serve, {'document_root': media_root, 'path': 'js/qunit/qunit.js'}, name='qunit_js'),
    url(r'^qunit/qunit.css', serve, {'document_root': media_root, 'path': 'css/qunit/qunit.css'}, name='qunit_css'),
    
    # jasmine
    url(r'^jasmine/(?P<app>[\w_]+)?$', 'jstest.views.suite_render', {'framework': 'jasmine'}),
    url(r'^jasmine/jasmine.js', serve, {'document_root': media_root, 'path': 'js/jasmine/jasmine.js'}, name='jasmine_js'),
    url(r'^jasmine/jasmine-html.js', serve, {'document_root': media_root, 'path': 'js/jasmine/jasmine-html.js'}, name='jasmine_html_js'),
    url(r'^jasmine/jasmine.css', serve, {'document_root': media_root, 'path': 'css/jasmine/jasmine.css'}, name='jasmine_css'),
)
