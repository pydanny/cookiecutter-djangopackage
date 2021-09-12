#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

from {{ cookiecutter.app_name }}/__init__ import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

{%- set license_classifiers = {
    "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License",
    "BSD": "License :: OSI Approved :: BSD License",
    "ISCL": "License :: OSI Approved :: ISC License (ISCL)",
    "MIT": "License :: OSI Approved :: MIT License",
} %}


def get_version(*file_paths):
    """Retrieves the version from {{ cookiecutter.app_name }}/__init__.py"""
    version_match = __version__
    if version_match:
        return version_match
    raise RuntimeError("Unable to find version string.")


version = get_version("{{ cookiecutter.app_name }}", "__init__.py")


if sys.argv[-1] == "publish":
    try:
        import wheel

        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print("Wheel library missing. Please run 'pip install wheel'")
        sys.exit()
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

if sys.argv[-1] == "tag":
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")
requirements = open("requirements.txt").readlines()

setup(
    name="{{ cookiecutter.repo_name }}",
    version=version,
    description="""{{ cookiecutter.project_short_description }}""",
    long_description=readme + "\n\n" + history,
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}",
    packages=[
        "{{ cookiecutter.app_name }}",
    ],
    include_package_data=True,
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    zip_safe=False,
    keywords="{{ cookiecutter.repo_name }}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
