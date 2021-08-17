# -*- coding: utf-8 -*-
from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name = '{{ cookiecutter.app_name }}'
urlpatterns = [
    {% if cookiecutter.models == "Comma-separated list of models" -%}
    path(r'', TemplateView.as_view(template_name="base.html")),
    {% else -%}
	{% for model in cookiecutter.models.split(',') -%}
    path(
        regex="^{{ model.strip() }}/~create/$",
        view=views.{{ model.strip() }}CreateView.as_view(),
        name='{{ model.strip() }}_create',
    ),
    path(
        regex="^{{ model.strip() }}/(?P<pk>\d+)/~delete/$",
        view=views.{{ model.strip() }}DeleteView.as_view(),
        name='{{ model.strip() }}_delete',
    ),
    path(
        regex="^{{ model.strip() }}/(?P<pk>\d+)/$",
        view=views.{{ model.strip() }}DetailView.as_view(),
        name='{{ model.strip() }}_detail',
    ),
    path(
        regex="^{{ model.strip() }}/(?P<pk>\d+)/~update/$",
        view=views.{{ model.strip() }}UpdateView.as_view(),
        name='{{ model.strip() }}_update',
    ),
    path(
        regex="^{{ model.strip() }}/$",
        view=views.{{ model.strip() }}ListView.as_view(),
        name='{{ model.strip() }}_list',
    ),
	{% endfor -%}
    {% endif -%}
]
