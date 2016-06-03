from contextlib import contextmanager
import shlex
import os
import subprocess
import datetime
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


def test_readme(cookies):
    extra_context = {'app_name': 'helloworld'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        readme_file = result.project.join('README.rst')
        readme_lines = [x.strip() for x in readme_file.readlines(cr=False)]
        assert 'Then use it in a project::' in readme_lines
        assert '(myenv) $ pip install -r requirements-test.txt' in readme_lines


def test_models(cookies):
    extra_context = {'models': 'ChocolateChip,Zimsterne', 'app_name': 'cookies'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        model_file = result.project.join('cookies', 'models.py')
        model_txt = model_file.read()
        assert 'TimeStampedModel' in model_txt


def test_views(cookies):
    pass

def test_urls(cookies):
    pass

def test_templates(cookies):
    pass


def test_travis(cookies):
    extra_context = {'app_name': 'cookie_lover'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        travis_file = result.project.join('.travis.yml')
        travis_text = travis_file.read()
        assert 'script: coverage run --source cookie_lover runtests.py' in travis_text


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
        assert "version = get_version('cookie_lover', '__init__.py')" in setup_text
        assert "    author='Cookie McCookieface'," in setup_text


## example project tests from here on
