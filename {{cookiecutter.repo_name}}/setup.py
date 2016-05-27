#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')

version = get_version('{{ cookiecutter.app_name }}', '__init__.py')

if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='{{ cookiecutter.repo_name }}',
    version=version,
    description="""{{ cookiecutter.project_short_description }}""",
    long_description=readme + '\n\n' + history,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=[
        '{{ cookiecutter.app_name }}',
    ],
    include_package_data=True,
    install_requires=[
        {% if cookiecutter.models != "Comma-separated list of models" %}
            "django-model-utils>=2.0",
        {% endif %}
    ],
    license="BSD",
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',{% if '1.7' in cookiecutter.django_versions %}
        'Framework :: Django :: 1.7',{% endif %}{% if '1.8' in cookiecutter.django_versions %}
        'Framework :: Django :: 1.8',{% endif %}{% if '1.9' in cookiecutter.django_versions %}
        'Framework :: Django :: 1.9',{% endif %}{% if '1.10' in cookiecutter.django_versions %}
        'Framework :: Django :: 1.10',{% endif %}
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',{% if '1.7' in cookiecutter.django_versions or '1.8' in cookiecutter.django_versions %}
        'Programming Language :: Python :: 3.3',{% endif %}
        'Programming Language :: Python :: 3.4',{% if '1.7' != cookiecutter.django_versions %}
        'Programming Language :: Python :: 3.5',{% endif %}
    ],
)
