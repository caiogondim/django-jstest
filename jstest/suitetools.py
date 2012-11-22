# coding: utf-8

import os
import fnmatch

from django.conf import settings
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.template import RequestContext


class FrameworkNotSupported(Exception):
    pass


class SuiteRender(object):

    SUPPORTED = ('qunit', 'jasmine')

    def __init__(self, framework=None, app=None):
        if framework in self.SUPPORTED:
            self.framework = framework
        else:
            raise FrameworkNotSupported('Framework %s not supported' % framework)

        self.app = app
        self.modules = self._get_modules_with_jstest()
        self.media = {"js": [], "css": []}
        self.tests = ""
        self.html = ""

        self._get_data()

    def _get_modules_with_jstest(self):
        apps = settings.INSTALLED_APPS
        modules = []

        if self.app is not None:
            if not self.app in apps:
                return []
            apps = [self.app]

        for a in apps:
            try:
                module = getattr(__import__("%s.tests" % a, locals(), globals(), ["jstest"], 3), "jstest")
                modules.append(module)
            except:
                pass

        return modules

    def _get_data(self):
        for m in self.modules:
            for top, dirs, files in os.walk(m.__path__[0]):
                self._parse_media_content(top, files)
                self._parse_tests(top, files)
                self._parse_fixtures(top, files)

    def _parse_media_content(self, top, files):
        json_name = "media.json"
        if json_name in files:
            content = simplejson.loads(open(os.path.join(top, json_name), 'r').read())
            self.media["js"] += content["js"]
            self.media["css"] += content["css"]

    # TODO: verificar arquivos em "files" com os prefixos "test_framework_"
    def _parse_tests(self, top, files):
        tests_name = "tests_%s.js" % self.framework
        if tests_name in files:
            self.tests += open(os.path.join(top, tests_name), 'r').read()

    def _parse_fixtures(self, top, files):
        html_name = "fixtures.html"
        if html_name in files:
            self.html += open(os.path.join(top, html_name), 'r').read()

    def to_browser(self, request):
        context = {
            'app': self.app,
            'media': self.media,
            'tests': self.tests,
            'html': self.html
        }

        return render_to_response(
            'jstest/%s/index.html' % self.framework, context,
            context_instance=RequestContext(request))

    def to_console(self):
        pass
