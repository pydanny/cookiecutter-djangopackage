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
    pass

def test_views(cookies):
    pass

def test_urls(cookies):
    pass

def test_templates(cookies):
    pass


def test_travis(cookies):
    pass


def test_authors(cookies):
    pass


def test_manifest(cookies):
    pass


def test_setup_py(cookies):
    pass


## example project tests from here on
