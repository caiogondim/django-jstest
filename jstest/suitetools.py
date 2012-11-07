# coding: utf-8

import os
import fnmatch

from django.conf import settings
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.template import RequestContext


class SuiteRender(object):

    SUPPORTED = ('qunit', 'jasmine')

    def __init__(self, framework=None, app=None):
        self.app = app

        if framework in self.SUPPORTED:
            self.framework = framework
        else:
            raise FrameworkNotSupported('Framework  %s not supported' % framework)
        self.modules = self._get_modules_with_jstest()

    def _get_modules_with_jstest(self):
        apps, modules = [a for a in settings.INSTALLED_APPS], []
        app = self.app

        if app is not None:
            if not app in apps:
                return []
            apps = [app]

        for a in apps:
            test_module_path = "%s.tests" % (a)
            try:
                module = getattr(__import__(test_module_path, locals(), globals(), ["js"], 3), "js")
                modules.append(module)
            except:
                pass

        return modules

    def _get_json_media(self):
        media = {"js": [], "css": []}
        json_name = "media.json"

        for m in self.modules:
            for top, dirs, files in os.walk(m.__path__[0] + "/" + self.framework):
                if json_name in files:
                    try:
                        content = simplejson.loads(open(os.path.join(top, json_name), 'r').read())
                        media["js"] += content["js"]
                        media["css"] += content["css"]
                    except:
                        pass

        return media

    def _get_tests(self):
        content = ""
        tests_name = "tests.js"

        for m in self.modules:
            for top, dirs, files in os.walk(m.__path__[0] + "/" + self.framework):
                try:
                    content += open(os.path.join(top, tests_name), 'r').read()
                except:
                    pass

        return content

    def _get_fixtures(self):
        content = ""
        html_name = "fixtures.html"

        for m in self.modules:
            for top, dirs, files in os.walk(m.__path__[0] + "/" + self.framework):
                try:
                    content += open(os.path.join(top, html_name), 'r').read()
                except:
                    pass

        return content

    def to_browser(self, request):
        context = {
            'app': self.app,
            'media': self._get_json_media(),
            'tests': self._get_tests(),
            'html': self._get_fixtures()
        }

        return render_to_response(
            'jstest/%s/index.html' % self.framework, context,
            context_instance=RequestContext(request))

    def to_console(self):
        pass
