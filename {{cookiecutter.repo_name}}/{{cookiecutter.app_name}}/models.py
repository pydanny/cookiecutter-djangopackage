# -*- coding: utf-8 -*-
{% if cookiecutter.models != "Comma-separated list of models" %}
from django.db import models

from model_utils.models import TimeStampedModel

{% for model in cookiecutter.models.split(',') %}
class {{ model.strip() }}(TimeStampedModel):
    pass
    
{% endfor %}
{% endif %}
