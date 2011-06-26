# coding: utf-8

from jstest.suitetools import SuiteRender


def suite_render(request, framework, app):
    render = SuiteRender(framework, app)
    return render.to_browser(request)