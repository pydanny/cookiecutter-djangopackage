#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import {{ cookiecutter.app_name }}
import commands

version = {{ cookiecutter.app_name }}.__version__

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
contributing = open('CONTRIBUTING.rst').read()

setup(
    name='{{ cookiecutter.project_name }}',
    version=version,
    description="""{{ cookiecutter.project_short_description }}""",
    long_description=readme + '\n\n' + history + '\n\n' + contributing,
    author='{{ cookiecutter.company_name }}',
    author_email='{{ cookiecutter.company_email }}',
    url='https://github.hogarthww.prv/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages('{{ cookiecutter.app_name }}', exclude=('tests',)),
    package_dir={'': '{{ cookiecutter.app_name }}'},
    include_package_data=True,
    install_requires=[
    ],
    test_requires=[
        'pytest'
    ],
    cmd_class={
        'test': commands.UnitTest
    },
    license="PROPRIETARY",
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Private :: Do Not Upload',
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
