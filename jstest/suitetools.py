# coding: utf-8

from django.conf import settings
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.template import RequestContext

from jstest.conf import DEFAULT_FRAMEWORK, SUPPORTED


class SuiteRender(object):
    
    def __init__(self, framework=None, app=None):
        self.app = app
        if framework in SUPPORTED:
            self.framework = framework
        else:
            self.framework = DEFAULT_FRAMEWORK

    def _get_modules_with_jstest(self):
        apps, modules = [a for a in settings.INSTALLED_APPS], []
        app = self.app
        
        if app != None:
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

    def _get_jslibs(self, modules):
        js = []
        for m in modules:
            json_file = "%s/jslibs.json" % (m.__path__[0])
            try:
                content = simplejson.loads(open(json_file, 'r').read())
                for src in content[0]["libs"]:
                    js.append(src)
            except:
                pass

        return js

    def _get_tests(self, modules):
        tests = ""
        for m in modules:
            tests_file_path = "%s/%s/tests.js" % (m.__path__[0], self.framework)
            try:
                tests += open(tests_file_path, 'r').read()
            except:
                pass
        
        return tests

    def to_browser(self, request):
        modules = self._get_modules_with_jstest()
        context = {
            'app': self.app,
            'jslibs': self._get_jslibs(modules),
            'tests': self._get_tests(modules)
        }
        
        return render_to_response(
            'jstest/%s/index.html' % self.framework, context,
            context_instance = RequestContext(request) )

    def to_console(self):
        pass

