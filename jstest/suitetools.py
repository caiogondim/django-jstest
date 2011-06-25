# coding: utf-8

from django.conf import settings

class SuiteRender(object):
    
    def __init__(self, framework=None, app=None):
        suported_frameworks = ['qunit', 'jasmine']
        self.app = app
        if framework in suported_frameworks:
            self.framework = framework
        else:
            self.framework = 'qunit' # default framework

    def get_apps_with_jstest(self):
        pass

    def to_console(self):
        pass
        
    def to_browser(self):
        pass
