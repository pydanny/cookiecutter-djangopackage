=====
Usage
=====

To use {{ cookiecutter.project_name }} in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        '{{ cookiecutter.app_name }}.apps.{{ cookiecutter.app_config_name }}',
        ...
    )

Add {{ cookiecutter.project_name }}'s URL patterns:

.. code-block:: python

    from {{ cookiecutter.app_name }} import urls as {{ cookiecutter.app_name }}_urls


    urlpatterns = [
        ...
        url(r'^', include({{ cookiecutter.app_name }}_urls)),
        ...
    ]
