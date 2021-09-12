# -*- coding: utf-8
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class {{ cookiecutter.app_config_name }}(AppConfig):
    name = "{{ cookiecutter.app_name }}"
    version_name = _("{{ cookiecutter.app_name }}")
