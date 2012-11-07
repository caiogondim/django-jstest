# coding: utf-8

from django.test import TestCase
from jstest.suitetools import SuiteRender


class SuiteRenderTest(TestCase):

    def test_initializing_suiterender_with_default_options(self):
        render = SuiteRender()
        self.assertEquals(render.framework, 'qunit')
        self.assertEquals(render.app, None)

    def test_initializing_suiterender_with_unsuported_framework_choose_the_default_one(self):
        render = SuiteRender('unsuported')
        self.assertEquals(render.framework, 'qunit')

    def test_initializing_suiterender_with_unknow_app(self):
        render = SuiteRender(app='unknow')
        self.assertEquals(render.app, None)
