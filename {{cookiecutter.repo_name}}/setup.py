# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
from setuptools import setup, find_packages

pkgmeta = {}
execfile(os.path.join(os.path.dirname(__file__),
         '{{ cookiecutter.app_name }}', 'pkgmeta.py'), pkgmeta)

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
    install_requires=[
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
)
