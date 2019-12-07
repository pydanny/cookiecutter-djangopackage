# -*- coding: utf-8 -*-
{% if cookiecutter.models != "Comma-separated list of models" %}
from django.contrib import admin

from .models import (
{% for model in cookiecutter.models.split(',') %}   {{ model.strip() }},
{% endfor %})

{% for model in cookiecutter.models.split(',') %}
@admin.register({{ model.strip() }})
class {{ model.strip() }}Admin(admin.ModelAdmin):
    pass

{% endfor %}
{% endif %}
