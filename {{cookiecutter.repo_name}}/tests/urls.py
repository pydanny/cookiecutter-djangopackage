# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from {{ cookiecutter.app_name }}.urls import urlpatterns as {{ cookiecutter.app_name }}_urls

urlpatterns = [
    url(r'^', include({{ cookiecutter.app_name }}_urls, namespace='{{ cookiecutter.app_name }}')),
]
