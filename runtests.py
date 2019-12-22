#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.core.management import execute_from_command_line
from django.test.utils import get_runner


def main():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    TestRunner = get_runner(settings)  # pylint: disable=invalid-name
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))


if __name__ == "__main__":
    main()