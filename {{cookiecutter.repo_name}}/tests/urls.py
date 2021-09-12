# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("{{ cookiecutter.app_name }}.urls", namespace="{{ cookiecutter.app_name }}")),
]
