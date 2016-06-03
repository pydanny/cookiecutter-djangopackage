# -*- coding: utf-8 -*-
{% if cookiecutter.models != "Comma-separated list of models" -%}
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import ({% for model in cookiecutter.models.split(',') %}
	{{ model.strip() }},{% endfor %}
)

{% set views = [
	'CreateView',
	'DeleteView',
	'DetailView',
	'UpdateView',
	'ListView'
] -%}

{% for model in cookiecutter.models.split(',') -%}
{% for view in views %}
class {{ model }}{{ view }}({{ view }}):

    model = {{ model }}

{% endfor -%}
{% endfor -%}
{% endif -%}
