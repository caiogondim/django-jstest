#-*- coding:utf-8 -*-

import os
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

from jstest.conf.scripts import JS_LIB_PATHS


def suite_render(request, app):
    apps, jslibs, modules = [], [], []
    exclude_apps = ("globocore", "contrib") + settings.EXCLUDE_TEST_APPS
    
    for a in settings.INSTALLED_APPS:
        if not a in exclude_apps:
            apps.append(a)

    if app != None:
        if not app in apps:
            raise Http404('Unknow app "%s".' % app)
        apps = [app]

    for item in apps:
        if item in JS_LIB_PATHS.keys():
            for src in JS_LIB_PATHS[item]:
                jslibs.append(src)

        test_module_path = "%s.tests" % (item)
        try:
            module = getattr(__import__(test_module_path, locals(), globals(), ["jsunit"], 3), "jsunit")
            modules.append(module)
        except:
            pass

    tests = ""
    for modulo in modules:
        tests_file_path = "%s/tests.js" % modulo.__path__[0]
        content = open(tests_file_path, 'r').readlines() 
        tests += "".join(content)

    context = { 'app': app, 'jslibs': jslibs, 'tests': tests }
    return render_to_response('jstest/qunit/suite_index.html', context, context_instance=RequestContext(request))
