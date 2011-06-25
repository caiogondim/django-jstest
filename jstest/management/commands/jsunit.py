# coding: utf-8

import os
from django.conf import settings
from django.utils import translation
from testutils.management.commands.base import ComandoDeTeste
# from django.core.management.base import BaseCommand
import jstest


class Command(ComandoDeTeste):
    pasta_dos_testes = ['jsunit']
    help = "Run js unit tests"

    def handle(self, *args, **options):
        translation.activate(settings.LANGUAGE_CODE)
        super(Command, self).handle(*args, **options)

    def roda_testes(self, options, pastas):
        local_url = "http://0.0.0.0:8000" # settings.BASE_URL
        path = jstest.__path__[0]
        run_tests_file = "%s/conf/qunit/run-tests.js" % path
        location = "%s/qunit/" % local_url

        f = open(run_tests_file, 'w')

        f.write("".join(["load('%s/conf/env.rhino.1.2.js');\n" % path,
                         "load('%s/conf/qunit/setup.js');\n" % path,
                         "window.location = '%s';" % location ]))
        f.close()

        ret = os.system("java -cp jstest/conf/rhino1_7R2/js.jar org.mozilla.javascript.tools.shell.Main -opt -1 -f %s" % run_tests_file)

        raise SystemExit(0 if ret == 0 else 1)
