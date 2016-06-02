# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

{% set views_names = ['Create', 'Delete', 'Detail', 'Update', 'List'] -%}

urlpatterns = [
    url(r'', TemplateView.as_view(template_name="base.html")),

	{% for model in cookiecutter.models.split(',') -%}
	{% for view in views_names -%}

    url(
        regex = "^{{ model.strip() }}/~{{ view.lower() }}$",
        view = views.{{ model.strip() }}{{ view }}View.as_view(),
        name = '{{ model.strip() }}_{{ view.lower() }}',
	),

    {% endfor %}
	{% endfor -%}

]

