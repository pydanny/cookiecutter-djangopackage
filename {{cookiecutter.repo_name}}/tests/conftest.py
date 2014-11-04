try:
    from django.conf import settings

    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "{{ cookiecutter.app_name }}.test.db"
            }
        },
        ROOT_URLCONF="{{ cookiecutter.app_name }}.urls",
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "{{ cookiecutter.app_name }}",
        ],
        SITE_ID=1,
        NOSE_ARGS=['-s'],
    )

    try:
        import django
        setup = django.setup
    except AttributeError:
        pass
    else:
        setup()

except ImportError:
    raise ImportError(
        "To fix this error, run: pip install -r requirements-test.txt"
    )
