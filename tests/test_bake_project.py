import os
from contextlib import contextmanager

import pytest
import sh
from cookiecutter.utils import rmtree


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies, cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def test_bake_selecting_license(cookies):
    """
    Test to check if the LICENSE gets the correct license selected
    """
    license_strings = {
        'Apache Software License 2.0': 'Apache',
        'BSD': 'Redistributions of source code must retain the above copyright notice, this',
        'ISCL': 'Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee',
        'MIT': 'MIT ',
    }
    for license, target_string in license_strings.items():
        with bake_in_temp_dir(cookies, extra_context={'open_source_license': license}) as result:
            assert target_string in result.project.join('LICENSE').read()
            assert license in result.project.join('setup.py').read()


def test_readme(cookies):
    extra_context = {'app_name': 'helloworld'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        readme_file = result.project.join('README.rst')
        readme_lines = [x.strip() for x in readme_file.readlines(cr=False)]
        assert 'Add it to your `INSTALLED_APPS`:' in readme_lines
        assert '(myenv) $ pip install tox' in readme_lines


def test_models(cookies):
    extra_context = {'models': 'ChocolateChip,Zimsterne', 'app_name': 'cookies'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        model_file = result.project.join('cookies', 'models.py')
        model_txt = model_file.read()
        assert 'TimeStampedModel' in model_txt



def test_views_with_models(cookies):
    """
    Test case to assert if the views are created when the models are passed
    """
    extra_context = {'models': 'Pug,Dog', 'app_name': 'cookies'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        views_file = result.project.join('cookies', 'views.py')
        views_file_txt = views_file.read()
        views = ['CreateView', 'DeleteView',
                 'DetailView', 'UpdateView', 'ListView']
        for view in views:
            assert 'Pug{}'.format(view) in views_file_txt
            assert 'Dog{}'.format(view) in views_file_txt


def test_views_without_models(cookies):
    """
    Test case to assert that the views.py file is empty when there are no models defined
    """
    extra_context = {'app_name': 'cookies'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        views_file = result.project.join('cookies', 'views.py')
        views_file_txt = views_file.read()
        assert views_file_txt == ''


def test_urls_regex_with_model(cookies):
    """
    Test case to assert that the urls.py file is created when models are passed
    """
    extra_context = {'models': 'Pug,Dog', 'app_name': 'cookies'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        urls_file = result.project.join('cookies', 'urls.py')
        urls_file_txt = urls_file.read()
        for model in extra_context['models'].split(','):
            assert '^{}/~create/$'.format(model) in urls_file_txt
            assert '^{}/(?P<pk>\d+)/~delete/$'.format(model) in urls_file_txt
            assert '^{}/(?P<pk>\d+)/$'.format(model) in urls_file_txt
            assert '^{}/(?P<pk>\d+)/~update/$'.format(model) in urls_file_txt
            assert '^{}/$'.format(model) in urls_file_txt


def test_urls_without_model(cookies):
    """
    Test case to assert that the urls.py file has the basic template when there are no models defined
    """
    extra_context = {'app_name': 'cookies'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        urls_file = result.project.join('cookies', 'urls.py')
        urls_file_txt = urls_file.read()
        basic_url = "url(r'', TemplateView.as_view(template_name=\"base.html\"))"
        assert basic_url in urls_file_txt


def test_templates(cookies):
    pass


def test_travis(cookies):
    extra_context = {'app_name': 'cookie_lover'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        travis_file = result.project.join('.travis.yml')
        travis_text = travis_file.read()
        assert 'script: tox -e $TOX_ENV' in travis_text


def test_tox(cookies):
    extra_context = {'app_name': 'cookie_lover'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        tox_file = result.project.join('tox.ini')
        tox_text = tox_file.read()
        assert 'commands = coverage run --source cookie_lover runtests.py' in tox_text


def test_authors(cookies):
    extra_context = {'full_name': 'Cookie McCookieface'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        authors_file = result.project.join('AUTHORS.rst')
        authors_text = authors_file.read()
        assert 'Cookie McCookieface' in authors_text

def test_manifest(cookies):
    extra_context = {'app_name': 'cookie_lover'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        manifest_file = result.project.join('MANIFEST.in')
        manifest_text = manifest_file.read()
        assert 'recursive-include cookie_lover *.html *.png *.gif *js *.css *jpg *jpeg *svg *py' in manifest_text


def test_setup_py(cookies):
    extra_context = {'app_name': 'cookie_lover', 'full_name': 'Cookie McCookieface'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        setup_file = result.project.join('setup.py')
        setup_text = setup_file.read()
        assert "version=version" in setup_text
        assert "    author='Cookie McCookieface'," in setup_text


def test_django_versions_default(cookies):
    """
    Test case to assert that the tox.ini & setup.py files are generated with correct versions w default Django versions
    """

    with bake_in_temp_dir(cookies) as result:

        tox_file = result.project.join('tox.ini')
        tox_text = tox_file.read()
        assert "{py27,py35,py36}-django-111" in tox_text
        assert "{py35,py36,py37}-django-21" in tox_text
        travis_file = result.project.join('.travis.yml')
        travis_text = travis_file.read()
        assert 'py35-django-111' in travis_text
        assert 'py36-django-111' in travis_text
        assert 'py35-django-21' in travis_text
        assert 'py36-django-21' in travis_text
        assert 'py37-django-21' in travis_text
        setup_file = result.project.join('setup.py')
        setup_text = setup_file.read()
        assert "'Framework :: Django :: 1.11'," in setup_text
        assert "'Framework :: Django :: 2.1'," in setup_text
        assert "'Programming Language :: Python :: 2'," in setup_text
        assert "'Programming Language :: Python :: 2.7'," in setup_text
        assert "'Programming Language :: Python :: 3'," in setup_text
        assert "'Programming Language :: Python :: 3.5'," in setup_text
        assert "'Programming Language :: Python :: 3.6'," in setup_text


def test_new_django_versions(cookies):
    """
    Test case to assert that the tox.ini & setup.py files are generated with correct versions with a new Django version
    """

    extra_context = {'django_versions': '1.11,2.1'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        tox_file = result.project.join('tox.ini')
        tox_text = tox_file.read()
        assert "{py27,py35,py36}-django-111" in tox_text
        assert 'django19' not in tox_text
        travis_file = result.project.join('.travis.yml')
        travis_text = travis_file.read()
        assert 'py27-django-111' in travis_text
        assert 'py35-django-111' in travis_text
        assert 'django19' not in travis_text
        setup_file = result.project.join('setup.py')
        setup_text = setup_file.read()
        assert "'Framework :: Django :: 2.1'," in setup_text
        assert "'Framework :: Django :: 1.11'," in setup_text
        assert "'Framework :: Django :: 1.9'," not in setup_text
        assert "'Programming Language :: Python :: 2'," in setup_text
        assert "'Programming Language :: Python :: 2.7'," in setup_text
        assert "'Programming Language :: Python :: 3'," in setup_text
        assert "'Programming Language :: Python :: 3.5'," in setup_text
        assert "'Programming Language :: Python :: 3.6'," in setup_text
        assert "'Programming Language :: Python :: 3.3'," not in setup_text


def test_flake8_compliance(cookies):
    """generated project should pass flake8"""
    extra_context = {'create_example_project': 'Y'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        for file_obj in result.project.listdir():
            name = os.path.join(
                file_obj.dirname,
                file_obj.basename
            )
            if not name.endswith('.py'):
                continue
            try:
                sh.flake8(name)
            except sh.ErrorReturnCode as e:
                pytest.fail(str(e))


def test_app_config(cookies):
    extra_context = {'app_name': 'cookie_lover'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        apps_file = result.project.join('cookie_lover', 'apps.py')
        apps_text = apps_file.read()
        assert 'CookieLoverConfig' in apps_text
        assert "name = 'cookie_lover'" in apps_text
        readme_file = result.project.join('README.rst')
        readme_text = readme_file.read()
        assert "'cookie_lover.apps.CookieLoverConfig'," in readme_text

# example project tests from here on

def test_make_migrations(cookies):
    """generated project should be able to generate migrations"""
    with bake_in_temp_dir(cookies, extra_context={}) as result:
        res = result.project.join('manage.py')
        try:
            sh.python(res, 'makemigrations')
        except sh.ErrorReturnCode as e:
            pytest.fail(str(e))


def test_run_tests(cookies):
    """generated project should run tests"""
    with bake_in_temp_dir(cookies, extra_context={}) as result:
        res = result.project.join('runtests.py')
        try:
            with res.dirpath().as_cwd():
                sh.python(res)
        except sh.ErrorReturnCode as e:
            pytest.fail(str(e))
