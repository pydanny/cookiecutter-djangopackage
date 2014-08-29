#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import subprocess


try:
    from setuptools import Command
except ImportError:
    from distutils.core import Command


class UnitTest(Command):
    description = 'run unit tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)
