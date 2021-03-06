# coding: utf-8

import os
from django.conf.urls.defaults import url, patterns


media_root = os.path.join(os.path.dirname(__file__), 'jstest_media')
serve = 'django.views.static.serve'

urlpatterns = patterns('',
    # qunit
    url(r'^jstest/qunit/(?P<app>[\w_]+)?$', 'jstest.views.suite_render', {'framework': 'qunit'}),
    url(r'^jstest/qunit/qunit\.js', serve, {'document_root': media_root, 'path': 'js/qunit/qunit.js'}, name='qunit_js'),
    url(r'^jstest/qunit/qunit\.css', serve, {'document_root': media_root, 'path': 'css/qunit/qunit.css'}, name='qunit_css'),

    # jasmine
    url(r'^jstest/jasmine/(?P<app>[\w_]+)?$', 'jstest.views.suite_render', {'framework': 'jasmine'}),
    url(r'^jstest/jasmine/jasmine\.js', serve, {'document_root': media_root, 'path': 'js/jasmine/jasmine.js'}, name='jasmine_js'),
    url(r'^jstest/jasmine/jasmine-html\.js', serve, {'document_root': media_root, 'path': 'js/jasmine/jasmine-html.js'}, name='jasmine_html_js'),
    url(r'^jstest/jasmine/jasmine\.css', serve, {'document_root': media_root, 'path': 'css/jasmine/jasmine.css'}, name='jasmine_css'),
)
