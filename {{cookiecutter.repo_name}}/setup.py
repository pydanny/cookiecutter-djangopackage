# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
from setuptools import setup, find_packages, Command
from setuptools.command.test import test as TestCommand
import sys


pkgmeta = {}
execfile(os.path.join(os.path.dirname(__file__),
         '{{ cookiecutter.app_name }}', 'pkgmeta.py'), pkgmeta)


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests', '-s']
        self.test_suite = True

    def run_tests(self):
        import pytest
        # Make sure this package's tests module gets priority.
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
        os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
        errno = pytest.main(self.test_args)
        sys.exit(errno)


class LintCommand(Command):
    """
    A copy of flake8's Flake8Command

    """
    description = "Run flake8 on modules registered in setuptools"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def distribution_files(self):
        if self.distribution.packages:
            for package in self.distribution.packages:
                yield package.replace(".", os.path.sep)

        if self.distribution.py_modules:
            for filename in self.distribution.py_modules:
                yield "%s.py" % filename


readme = open('README.rst').read()

setup(
    name=pkgmeta['__title__'],
    version=pkgmeta['__version__'],
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme,
    author=pkgmeta['__author__'],
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=[
        'flake8',
    ],
    tests_require=[
        'pytest-django',
    ],
    install_requires=[
        'Django>=1.2',
    ],
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    cmdclass={
        'test': PyTest,
        'lint': LintCommand,
    },
)
